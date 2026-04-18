--Ucraniano de Família
local s,id=GetID()
function s.initial_effect(c)

	-- FLIP: recuperar + possível ativação
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCode(EVENT_FLIP)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.flipcon)
	e1:SetTarget(s.fliptg)
	e1:SetOperation(s.flipop)
	c:RegisterEffect(e1)

	-- Quando Invocado: virar para baixo + normal summon extra + marcar flip automático
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
	e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
	e2:SetCode(EVENT_SUMMON_SUCCESS)
	e2:SetOperation(s.sumop)
	c:RegisterEffect(e2)

	local e3=e2:Clone()
	e3:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e3)

	-- Se deixar o campo: recuperar monstro Universo G
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,1))
	e4:SetCategory(CATEGORY_TOHAND)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCode(EVENT_LEAVE_FIELD)
	e4:SetCountLimit(1,id+200)
	e4:SetCondition(s.leavecon)
	e4:SetTarget(s.leavetg)
	e4:SetOperation(s.leaveop)
	c:RegisterEffect(e4)

	-- Quick Effect: virar 1 monstro para cima
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,2))
	e5:SetType(EFFECT_TYPE_QUICK_O)
	e5:SetCode(EVENT_FREE_CHAIN)
	e5:SetRange(LOCATION_MZONE)
	e5:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e5:SetCountLimit(1,id+400)
	e5:SetCondition(s.qpcon)
	e5:SetTarget(s.qptg)
	e5:SetOperation(s.qpop)
	c:RegisterEffect(e5)
end

function s.flipcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetCurrentPhase()==PHASE_END
end

function s.thfilter(c)
	return c:IsAbleToHand()
		and (
			c:IsLocation(LOCATION_GRAVE)
			or c:IsLocation(LOCATION_REMOVED)
			or (c:IsLocation(LOCATION_EXTRA) and c:IsFaceup())
		)
end

function s.fliptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,
			LOCATION_GRAVE+LOCATION_REMOVED+LOCATION_EXTRA,0,1,nil)
	end
	-- Declara add from GY/Removed/Extra para Ghost Belle
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_GRAVE+LOCATION_REMOVED+LOCATION_EXTRA)
end

function s.flipop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,
		LOCATION_GRAVE+LOCATION_REMOVED+LOCATION_EXTRA,0,1,1,nil)
	local tc=g:GetFirst()
	if not tc then return end

	if Duel.SendtoHand(tc,nil,REASON_EFFECT)>0 then
		Duel.ConfirmCards(1-tp,tc)

		local c=e:GetHandler()
		local g2=Duel.GetMatchingGroup(function(mc)
			return mc:IsFaceup() and mc:IsLocation(LOCATION_MZONE) and mc~=c
		end,tp,LOCATION_MZONE,0,nil)

		if #g2>0 and Duel.SelectYesNo(tp,aux.Stringid(id,2)) then
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_POSCHANGE)
			local sg=g2:Select(tp,1,1,nil)
			if #sg>0 then
				Duel.ChangePosition(sg,POS_FACEDOWN_DEFENSE)
			end
		end
	end
end

function s.sumop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	-- Virar para baixo
	if c:IsFaceup() then
		Duel.ChangePosition(c,POS_FACEDOWN_DEFENSE)
	end

	-- Normal summon adicional Universo G
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_EXTRA_SUMMON_COUNT)
	e1:SetTargetRange(LOCATION_HAND+LOCATION_MZONE,0)
	e1:SetTarget(function(e,c)
		return c:IsSetCard(0xc50)
	end)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)

	-- Flip automático na End Phase
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e2:SetCode(EVENT_PHASE+PHASE_END)
	e2:SetCountLimit(1)
	e2:SetOperation(function(e,tp)
		if c:IsLocation(LOCATION_MZONE)
			and c:IsFacedown() then
			Duel.ChangePosition(c,POS_FACEUP_DEFENSE)
		end
	end)
	e2:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e2,tp)
end

function s.leavecon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_ONFIELD)
end

function s.leavefilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_MONSTER)
		and c:IsAbleToHand()
		and (
			c:IsLocation(LOCATION_GRAVE)
			or c:IsLocation(LOCATION_REMOVED)
			or (c:IsLocation(LOCATION_EXTRA) and c:IsFaceup())
		)
end

function s.leavetg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.leavefilter,tp,
			LOCATION_GRAVE+LOCATION_REMOVED+LOCATION_EXTRA,0,1,nil)
	end
end

function s.leaveop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.leavefilter,tp,
		LOCATION_GRAVE+LOCATION_REMOVED+LOCATION_EXTRA,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
end

function s.qpcon(e,tp,eg,ep,ev,re,r,rp)
	local ph=Duel.GetCurrentPhase()
	return ph==PHASE_MAIN1 or ph==PHASE_MAIN2
end

function s.qpfilter(c)
	return c:IsFacedown() and c:IsAbleToHand()
end

function s.qptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(tp) and s.qpfilter(chkc) end
	if chk==0 then
		return Duel.IsExistingTarget(s.qpfilter,tp,LOCATION_MZONE,0,1,nil)
			and Duel.GetLocationCount(tp,LOCATION_MZONE)>-1
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	Duel.SelectTarget(tp,s.qpfilter,tp,LOCATION_MZONE,0,1,1,nil)
end

function s.qpop(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	if not tc or not tc:IsRelateToEffect(e) then return end

	if Duel.SendtoHand(tc,nil,REASON_EFFECT)>0 then
		Duel.ConfirmCards(1-tp,tc)

		-- Verifica se ainda pode invocar
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
		if not tc:IsSummonable(true,nil) then return end

		-- Pergunta ao jogador
		if Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
			Duel.Summon(tp,tc,true,nil)
		end
	end
end
