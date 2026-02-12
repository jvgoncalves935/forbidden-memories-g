--Paulo Gino Piscineiro
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()

	-- Link Summon
	aux.AddLinkProcedure(c,s.matfilter,1,1)
	
	-- 1) Link Summon → revive Link "Universo G" (HOPT)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(s.spcon1)
	e1:SetTarget(s.sptg1)
	e1:SetOperation(s.spop1)
	e1:SetCountLimit(1,id)
	c:RegisterEffect(e1)

	-- 2) Contínuo obrigatório: se o oponente adicionar/comprar no seu turno → você compra
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e2:SetCode(EVENT_DRAW)
	e2:SetRange(LOCATION_MZONE)
	e2:SetCondition(s.drcon)
	e2:SetOperation(s.drop)
	e2:SetCountLimit(1,id+200)
	c:RegisterEffect(e2)

	-- 3) Quick: pagar 1500 + tributar → recuperar Extra (HOPT)
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetCategory(CATEGORY_TOHAND)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id+400)
	e3:SetCost(s.thcost)
	e3:SetTarget(s.thtg)
	e3:SetOperation(s.thop)
	c:RegisterEffect(e3)
end

-- Material Link
function s.matfilter(c,lc,sumtype,tp)
	return c:IsSetCard(0xc50)
end

-- 1) Link Summon revive
function s.spcon1(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_LINK)
end

function s.spfilter1(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_LINK)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

function s.sptg1(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingTarget(s.spfilter1,tp,LOCATION_GRAVE,0,1,nil,e,tp)
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectTarget(tp,s.spfilter1,tp,LOCATION_GRAVE,0,1,1,nil,e,tp)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,g,1,0,0)
end

function s.spop1(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	if tc and tc:IsRelateToEffect(e) then
		Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
	end
end

-- 2) Oponente comprou/adicionou no seu turno → você compra
function s.drcon(e,tp,eg,ep,ev,re,r,rp)
	return ep==1-tp				 -- oponente comprou
		and Duel.GetTurnPlayer()==tp -- é seu turno
end

function s.drop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Draw(tp,1,REASON_EFFECT)
end

-- 3) Quick: pagar 1500 + tributar → recuperar Extra
function s.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.CheckLPCost(tp,1500)
			and c:IsReleasable()
	end
	Duel.PayLPCost(tp,1500)
	Duel.Release(c,REASON_COST)
end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsFaceup()
		and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_EXTRA,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_EXTRA)
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_EXTRA,0,1,1,nil)
	local tc=g:GetFirst()
	if tc then
		Duel.SendtoHand(tc,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,tc)
	end
end

