--Ricco Puentes, The King Of Gueis
local s,id=GetID()

function s.initial_effect(c)
	c:EnableReviveLimit()
	c:SetUniqueOnField(1,0,id)

	-- Xyz padrão
	aux.AddXyzProcedureLevelFree(c, s.mfilter, nil, 2, 2)

	-- Contact Xyz (1x por duelo)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_EXTRA)
	e1:SetCondition(s.ctcon)
	e1:SetTarget(s.cttg)
	e1:SetOperation(s.ctop)
	c:RegisterEffect(e1)

	-- Aplica lock se for Contact
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	e2:SetOperation(s.lockop)
	c:RegisterEffect(e2)

	-- Quick Effect
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetCategory(CATEGORY_REMOVE)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id+200)
	e3:SetCost(s.qcost)
	e3:SetOperation(s.qop)
	c:RegisterEffect(e3)

end

-- Filtro material
function s.mfilter(c,xyzc)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_NORMAL)
end

function s.cfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_NORMAL)
		and c:IsAbleToHand()
end

function s.ctcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if Duel.GetFlagEffect(tp,id+600)~=0 then return false end

	local g=Duel.GetMatchingGroup(s.cfilter,tp,
		LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED,0,nil)

	if #g<2 then return false end

	-- apenas monstros no campo podem liberar zona
	local fg=g:Filter(Card.IsLocation,nil,LOCATION_MZONE)

	return Duel.GetLocationCountFromEx(tp,tp,fg,c)>0
end

function s.cttg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,2,tp,
		LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,tp,LOCATION_EXTRA)
end

function s.ctop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local g=Duel.SelectMatchingCard(tp,s.cfilter,tp,
		LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED,0,2,2,nil)
	if #g~=2 then return end
	if Duel.SendtoHand(g,nil,REASON_COST)==0 then return end

	Duel.ConfirmCards(1-tp,g)

	if Duel.SpecialSummon(c,SUMMON_TYPE_XYZ,tp,tp,false,false,POS_FACEUP)==0 then return end
	c:CompleteProcedure()
	
	-- Marca Contact usada (1x por duelo real)
	Duel.RegisterFlagEffect(tp,id+600,0,0,0)

	-- Marca que foi Contact
	c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD,0,1)
end

-- Bloqueia invocações não-Universo G
function s.splimit(e,c)
	return not c:IsSetCard(0xc50)
end

function s.lockop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	-- Só se foi Contact
	if c:GetFlagEffect(id)==0 then return end

	-- Lock 1x por duelo
	if Duel.GetFlagEffect(tp,id+400)>0 then return end
	Duel.RegisterFlagEffect(tp,id+400,0,0,0)

	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_CANNOT_SUMMON)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e1:SetTargetRange(1,0)
	e1:SetTarget(s.splimit)
	Duel.RegisterEffect(e1,tp)

	local e2=e1:Clone()
	e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	Duel.RegisterEffect(e2,tp)

	local e3=e1:Clone()
	e3:SetCode(EFFECT_CANNOT_FLIP_SUMMON)
	Duel.RegisterEffect(e3,tp)
end

function s.revfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_NORMAL)
		and not c:IsPublic()
end

function s.qcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.revfilter,tp,LOCATION_HAND,0,2,nil)
			and Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,2,nil)
	end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local g1=Duel.SelectMatchingCard(tp,s.revfilter,tp,LOCATION_HAND,0,2,2,nil)
	Duel.ConfirmCards(1-tp,g1)
	Duel.ShuffleHand(tp)

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DISCARD)
	local g2=Duel.SelectMatchingCard(tp,Card.IsDiscardable,tp,LOCATION_HAND,0,2,2,nil)
	Duel.SendtoGrave(g2,REASON_COST+REASON_DISCARD)
end

function s.qop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local g=Duel.SelectMatchingCard(tp,Card.IsFaceup,tp,
		LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,nil)
	local tc=g:GetFirst()
	if not tc then return end

	if tc:IsFaceup() and tc:IsCanBeDisabledByEffect(e) then
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_DISABLE)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		tc:RegisterEffect(e1)

		local e2=Effect.CreateEffect(c)
		e2:SetType(EFFECT_TYPE_SINGLE)
		e2:SetCode(EFFECT_DISABLE_EFFECT)
		e2:SetValue(RESET_TURN_SET)
		e2:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		tc:RegisterEffect(e2)

		if tc:IsType(TYPE_TRAPMONSTER) then
			local e3=Effect.CreateEffect(c)
			e3:SetType(EFFECT_TYPE_SINGLE)
			e3:SetCode(EFFECT_DISABLE_TRAPMONSTER)
			e3:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			tc:RegisterEffect(e3)
		end

		Duel.AdjustInstantly()
		Duel.NegateRelatedChain(tc,RESET_TURN_SET)
	end

	if tc:IsOnField() then
		Duel.Remove(tc,POS_FACEUP,REASON_EFFECT)
	end

	if c:IsOnField() then
		Duel.Remove(c,POS_FACEUP,REASON_EFFECT)
	end
end