--Danger!? Gilson?
local s,id=GetID()
function s.initial_effect(c)

	-- Quick Effect Win Condition / Fusion
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id) -- hard OPT
	e1:SetCondition(s.wincon)
	e1:SetOperation(s.winop)
	c:RegisterEffect(e1)

	-- If used as Fusion Material: place Universo G S/T
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,5))
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_BE_MATERIAL)
	e2:SetCountLimit(1,id+200) -- hard OPT (segundo efeito)
	e2:SetCondition(s.ufcon)
	e2:SetTarget(s.uftg)
	e2:SetOperation(s.ufop)
	c:RegisterEffect(e2)

end

-- Condição: existe Fusão Universo G válida
function s.fusionfilter(c)
	return c:IsType(TYPE_FUSION)
		and c:IsSetCard(0xc50)
		and c:IsLevelBelow(8)
end

function s.wincon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsExistingMatchingCard(
		s.fusionfilter,tp,LOCATION_EXTRA,0,1,nil
	)
end

-- Operação principal
function s.winop(e,tp,eg,ep,ev,re,r,rp)

	local opt=Duel.SelectOption(
		1-tp,
		aux.Stringid(id,2), -- "Dizer 'Gilson?'"
		aux.Stringid(id,3)  -- "Não dizer 'Gilson?'"
	)

	-- Oponente disse "Gilson?"
	if opt==0 then

		-- Seleciona o monstro Fusão
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local fc=Duel.SelectMatchingCard(
			tp,s.fusionfilter,tp,LOCATION_EXTRA,0,1,1,nil
		):GetFirst()
		if not fc then return end

		-- Seleciona 1 matéria da mão
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
		local mg1=Duel.SelectMatchingCard(
			tp,s.matfilter,tp,LOCATION_HAND,0,1,1,nil
		):GetFirst()
		if not mg1 then return end

		-- Seleciona 1 matéria do Deck
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
		local mg2=Duel.SelectMatchingCard(
			tp,s.matfilter,tp,LOCATION_DECK,0,1,1,nil
		):GetFirst()
		if not mg2 then return end


		local mat=Group.FromCards(mg1,mg2)
		fc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_FUSION)

		Duel.BreakEffect()
		Duel.SpecialSummon(fc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)
		fc:CompleteProcedure()

		-- Lock de Fusões
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_FIELD)
		e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
		e1:SetTargetRange(1,0)
		e1:SetTarget(s.splimit_fusion)
		e1:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e1,tp)

		-- Lock Universo G
		local e2=Effect.CreateEffect(e:GetHandler())
		e2:SetType(EFFECT_TYPE_FIELD)
		e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
		e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
		e2:SetTargetRange(1,0)
		e2:SetTarget(s.splimit_universo)
		e2:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e2,tp)

		return
	end

	-- Oponente NÃO disse "Gilson?"
	Duel.Hint(HINT_MESSAGE,tp,aux.Stringid(id,4))
	Duel.Win(tp,0x690)
end

function s.splimit_fusion(e,c,sump,sumtype,sumpos,targetp,se)
	return c:IsType(TYPE_FUSION)
end

function s.splimit_universo(e,c,sump,sumtype,sumpos,targetp,se)
	return not c:IsSetCard(0xc50)
end

function s.matfilter(c)
	return c:IsType(TYPE_MONSTER)
end

function s.ufcon(e,tp,eg,ep,ev,re,r,rp)
	return r & REASON_FUSION ~= 0
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

	local zone=LOCATION_SZONE
	if tc:IsType(TYPE_FIELD) then
		zone=LOCATION_FZONE
	end

	Duel.MoveToField(
		tc,tp,tp,
		zone,
		POS_FACEUP,
		true
	)
end

