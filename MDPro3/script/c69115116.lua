--Danger!? Gilson?
local s,id=GetID()
function s.initial_effect(c)

	-- Quick Effect Win Condition / Fusion
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON+CATEGORY_DECKDES)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.wincon)
	e1:SetOperation(s.winop)
	c:RegisterEffect(e1)

	-- If used as Synchro/Fusion/Link Material
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,5))
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_BE_MATERIAL)
	e2:SetRange(LOCATION_GRAVE)
	e2:SetCountLimit(1,id+200)
	e2:SetCondition(s.ufcon)
	e2:SetTarget(s.uftg)
	e2:SetOperation(s.ufop)
	c:RegisterEffect(e2)

end

function s.fusionfilter(c,e,tp)
	return c:IsType(TYPE_FUSION)
		and c:IsSetCard(0xc50)
		and c:IsLevelBelow(8)
		and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0
		and s.checkfusionpossible(c,tp)
end

-- Verifica se existe combinação válida:
-- 1 da mão/campo + 1 do Deck
function s.checkfusionpossible(fc,tp)

	local g1=Duel.GetMatchingGroup(Card.IsType,tp,LOCATION_HAND+LOCATION_MZONE,0,nil,TYPE_MONSTER)
	local g2=Duel.GetMatchingGroup(Card.IsType,tp,LOCATION_DECK,0,nil,TYPE_MONSTER)

	local c1=g1:GetFirst()
	while c1 do

		local c2=g2:GetFirst()
		while c2 do

			local mat=Group.FromCards(c1,c2)
			if fc:CheckFusionMaterial(mat,nil,tp) then
				return true
			end

			c2=g2:GetNext()
		end

		c1=g1:GetNext()
	end

	return false
end

function s.wincon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsExistingMatchingCard(
		s.fusionfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp
	)
end

function s.winop(e,tp,eg,ep,ev,re,r,rp)

	local opt=Duel.SelectOption(
		1-tp,
		aux.Stringid(id,2),
		aux.Stringid(id,3)
	)

	-- Oponente disse "Gilson?"
	if opt==0 then

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local fc=Duel.SelectMatchingCard(
			tp,s.fusionfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp
		):GetFirst()
		if not fc then return end

		-- Primeiro material (mão/campo) FORÇADO a ser válido
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
		local mg1=Duel.SelectMatchingCard(
			tp,
			function(c,fc,tp)
				if not c:IsType(TYPE_MONSTER) then return false end
				local g2=Duel.GetMatchingGroup(Card.IsType,tp,LOCATION_DECK,0,nil,TYPE_MONSTER)
				local tc=g2:GetFirst()
				while tc do
					local mat=Group.FromCards(c,tc)
					if fc:CheckFusionMaterial(mat,nil,tp) then
						return true
					end
					tc=g2:GetNext()
				end
				return false
			end,
			tp,LOCATION_HAND+LOCATION_MZONE,0,1,1,nil,fc,tp
		):GetFirst()
		if not mg1 then return end

		-- Segundo material (Deck) garantido válido
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
		local mg2=Duel.SelectMatchingCard(
			tp,
			function(c,mg1,fc,tp)
				if not c:IsType(TYPE_MONSTER) then return false end
				local mat=Group.FromCards(mg1,c)
				return fc:CheckFusionMaterial(mat,nil,tp)
			end,
			tp,LOCATION_DECK,0,1,1,nil,mg1,fc,tp
		):GetFirst()
		if not mg2 then return end

		local mat=Group.FromCards(mg1,mg2)

		fc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_FUSION)

		Duel.BreakEffect()

		Duel.SpecialSummon(fc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)
		fc:CompleteProcedure()

		-- Lock: não pode Invocar Fusão
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_FIELD)
		e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
		e1:SetTargetRange(1,0)
		e1:SetTarget(function(e,c) return c:IsType(TYPE_FUSION) end)
		e1:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e1,tp)

		-- Lock: só Universo G
		local e2=Effect.CreateEffect(e:GetHandler())
		e2:SetType(EFFECT_TYPE_FIELD)
		e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
		e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
		e2:SetTargetRange(1,0)
		e2:SetTarget(function(e,c) return not c:IsSetCard(0xc50) end)
		e2:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e2,tp)

		return
	end

	-- Oponente NÃO disse "Gilson?"
	Duel.Hint(HINT_MESSAGE,tp,aux.Stringid(id,4))
	Duel.Win(tp,0x690)
end


-- EFEITO DE MATERIAL
function s.ufcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsReason(REASON_MATERIAL)
		and c:IsReason(REASON_SYNCHRO+REASON_FUSION+REASON_LINK)
end

function s.ufilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SPELL+TYPE_TRAP)
		and (c:IsType(TYPE_CONTINUOUS) or c:IsType(TYPE_FIELD))
		and not c:IsForbidden()
end

function s.uftg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(
			s.ufilter,tp,
			LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,
			0,1,nil
		)
	end
end

function s.ufop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
	local tc=Duel.SelectMatchingCard(
		tp,s.ufilter,tp,
		LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,
		0,1,1,nil
	):GetFirst()
	if not tc then return end

	local opt=Duel.SelectOption(tp,aux.Stringid(id,5),aux.Stringid(id,6))

	if opt==1 then
		if tc:IsSSetable() then
			Duel.SSet(tp,tc)
		end
		return
	end

	local zone=LOCATION_SZONE
	if tc:IsType(TYPE_FIELD) then
		zone=LOCATION_FZONE
	end

	Duel.MoveToField(tc,tp,tp,zone,POS_FACEUP,true)
end