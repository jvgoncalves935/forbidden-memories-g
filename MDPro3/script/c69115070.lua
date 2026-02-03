-- Jailson Mendes, O Primeiro Machinho
local s,id=GetID()

function s.initial_effect(c)
	c:EnableReviveLimit()

	-- Link Summon: 4 monstros "Universo G"
	aux.AddLinkProcedure(c,s.matfilter,4,4)
	
	-- Nome alternativo no campo e GY
	aux.EnableChangeCode(c,69115007,LOCATION_MZONE+LOCATION_GRAVE)

	-- Ao ser Invocado por Link: comprar 5, devolver 3 (soft OPT)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_DRAW)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCountLimit(1)
	e1:SetCondition(s.drcon)
	e1:SetTarget(s.drtg)
	e1:SetOperation(s.drop)
	c:RegisterEffect(e1)

	-- Enviar 1 da mão ou campo → reviver Link Universo G (soft OPT)
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_IGNITION)
	e2:SetRange(LOCATION_MZONE)
	e2:SetCountLimit(1)
	e2:SetCost(s.spcost)
	e2:SetTarget(s.sptg)
	e2:SetOperation(s.spop)
	c:RegisterEffect(e2)

	-- Negar ativação até 2x por turno + perder 400 ATK (Quick)
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_CHAINING)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(2)
	e3:SetCondition(s.negcon)
	e3:SetTarget(s.negtg)
	e3:SetOperation(s.negop)
	c:RegisterEffect(e3)
end

-- Material Link
function s.matfilter(c,lc,sumtype,tp)
	return c:IsSetCard(0xc50)
end

-- ===== Efeito 1: Comprar 5 / devolver 3 =====
function s.drcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_LINK)
end

function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,5) end
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,5)
end

function s.drop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.Draw(tp,5,REASON_EFFECT)==0 then return end
	Duel.ShuffleHand(tp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local g=Duel.SelectMatchingCard(tp,Card.IsAbleToDeck,tp,LOCATION_HAND,0,3,3,nil)
	Duel.SendtoDeck(g,nil,SEQ_DECKBOTTOM,REASON_EFFECT)
end

-- ===== Efeito 2: Reviver Link =====
function s.costfilter(c)
	return c:IsAbleToGrave()
end

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.costfilter,tp,LOCATION_HAND+LOCATION_MZONE,0,1,c)
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local g=Duel.SelectMatchingCard(tp,s.costfilter,tp,LOCATION_HAND+LOCATION_MZONE,0,1,1,c)
	Duel.SendtoGrave(g,REASON_COST)
end

function s.spfilter(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_LINK)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_GRAVE,0,1,nil,e,tp)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_GRAVE)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_GRAVE,0,1,1,nil,e,tp)
	local tc=g:GetFirst()
	if tc then
		Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
	end
end

-- ===== Efeito 3: Negar + perder ATK =====
function s.negcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsChainNegatable(ev)
end

function s.negtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)
end

function s.negop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	Duel.NegateActivation(ev)

	-- Perde 400 ATK permanentemente
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_UPDATE_ATTACK)
	e1:SetValue(-400)
	c:RegisterEffect(e1)
end