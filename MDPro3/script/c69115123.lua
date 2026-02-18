-- Yami Senna
local s,id=GetID()

function s.initial_effect(c)
	c:EnableReviveLimit()

	-- Sempre tratado como múltiplos arquétipos
	aux.AddCodeList(c,69115001)

	-- Link-4: "Alexandre Senna" + 1+ monstros
	aux.AddLinkProcedure(c,s.lfilter,2,4,s.lcheck)

	-- Não pode controlar "Alexandre Senna"
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e1:SetCode(EVENT_ADJUST)
	e1:SetRange(LOCATION_MZONE)
	e1:SetOperation(s.limitop)
	c:RegisterEffect(e1)

	-- Negar Magias/Armadilhas face-up ao entrar (sem chain)
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	e2:SetCondition(s.negcon)
	e2:SetOperation(s.negop)
	c:RegisterEffect(e2)

	-- Retornar cards igual ao nº de materiais (exceto Alexandre)
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_SPSUMMON_SUCCESS)
	e3:SetCondition(s.bouncecon)
	e3:SetTarget(s.bouncetg)
	e3:SetOperation(s.bounceop)
	e3:SetCountLimit(1,id+200)
	c:RegisterEffect(e3)

	-- Se enviado ao GY: Invocar Link-2 ou menos "Universo G"
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,2))
	e4:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCode(EVENT_TO_GRAVE)
	e4:SetCountLimit(1,id+400)
	e4:SetCondition(s.spcon)
	e4:SetTarget(s.sptg)
	e4:SetOperation(s.spop)
	c:RegisterEffect(e4)

end

function s.limitop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local g=Duel.GetMatchingGroup(Card.IsCode,tp,LOCATION_MZONE,0,c,69115001)
	if #g>0 then
		Duel.SendtoGrave(g,REASON_RULE)
	end
end

function s.lfilter(c,lc,sumtype,tp)
	return c:IsType(TYPE_MONSTER)
end

function s.lcheck(g,lc,sumtype,tp)
	return g:IsExists(Card.IsCode,1,nil,69115001)
end

function s.negcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_LINK)
end

function s.negop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(
		function(c)
			return c:IsFaceup()
				and (c:IsType(TYPE_SPELL) or c:IsType(TYPE_TRAP))
		end,
		tp,0,LOCATION_ONFIELD,nil
	)
	for tc in aux.Next(g) do
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_DISABLE)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
		tc:RegisterEffect(e1)

		local e2=e1:Clone()
		e2:SetCode(EFFECT_DISABLE_EFFECT)
		tc:RegisterEffect(e2)
	end

end

function s.bouncecon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_LINK)
end

function s.bouncetg(e,tp,eg,ep,ev,re,r,rp,chk)
	local mg=e:GetHandler():GetMaterial()
	local ct=mg:FilterCount(function(tc)
		return not tc:IsCode(69115001)
	end,nil)

	if chk==0 then
		return ct>0 and Duel.IsExistingMatchingCard(
			Card.IsAbleToDeck,tp,
			LOCATION_ONFIELD,LOCATION_ONFIELD,1,nil
		)
	end
	e:SetLabel(ct)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,nil,ct,PLAYER_ALL,LOCATION_ONFIELD)
end

function s.bounceop(e,tp,eg,ep,ev,re,r,rp)
	local ct=e:GetLabel()
	if ct<=0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local g=Duel.SelectMatchingCard(
		tp,Card.IsAbleToDeck,
		tp,LOCATION_ONFIELD,LOCATION_ONFIELD,
		1,math.min(ct,Duel.GetMatchingGroupCount(Card.IsAbleToDeck,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil)),
		nil
	)

	if #g>0 then
		Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
	end
end

function s.spfilter(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_LINK)
		and c:GetLink()<=2
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsLocation(LOCATION_GRAVE) and
		(c:IsPreviousLocation(LOCATION_ONFIELD)
		or c:IsPreviousLocation(LOCATION_HAND)
		or c:IsPreviousLocation(LOCATION_DECK)
		or c:IsPreviousLocation(LOCATION_EXTRA)
		or c:IsPreviousLocation(LOCATION_REMOVED)
		or c:IsPreviousLocation(LOCATION_OVERLAY))
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingMatchingCard(
				s.spfilter,tp,LOCATION_GRAVE,0,1,nil,e,tp
			)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_GRAVE)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(
		tp,s.spfilter,tp,LOCATION_GRAVE,0,1,1,nil,e,tp
	)
	local tc=g:GetFirst()
	if tc then
		Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
	end
end
