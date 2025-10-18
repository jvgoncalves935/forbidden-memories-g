--Kid Bengala, O Grande
--c69115020
local s,id=GetID()
function s.initial_effect(c)
	--Permite ser usado como monstro Pêndulo
	aux.EnablePendulumAttribute(c)

	---------------------------------------------------------------
	--Efeito 1: Ao ser Invocado, busca 1 monstro "Universo G" do Deck
	---------------------------------------------------------------
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetTarget(s.thtg)
	e1:SetOperation(s.thop)
	c:RegisterEffect(e1)

	---------------------------------------------------------------
	--Efeito 2: Efeito Rápido da mão, Invocação-Ritual
	---------------------------------------------------------------
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetRange(LOCATION_HAND)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetCountLimit(1,id)
	e2:SetTarget(s.ritualtg)
	e2:SetOperation(s.ritualop)
	c:RegisterEffect(e2)

	---------------------------------------------------------------
	--Efeito 3: Efeito Rápido do campo para Zona de Pêndulo
	---------------------------------------------------------------
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetCountLimit(1,id+100)
	e3:SetTarget(s.moveptg)
	e3:SetOperation(s.movepop)
	c:RegisterEffect(e3)
end

---------------------------------------------------------------
-- [Efeito 1] – Buscar monstro "Universo G"
---------------------------------------------------------------
function s.thfilter(c)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_MONSTER) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end
function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
end

---------------------------------------------------------------
-- [Efeito 2] – Ritual da mão
---------------------------------------------------------------
function s.ritualtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_RITUAL,tp,true,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_RELEASE,c,1,0,0)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.ritualop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end

	-- Tributar da mão
	if Duel.Release(c,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)==0 then return end

	-- Ritual Summon do próprio card
	Duel.SpecialSummonStep(c,SUMMON_TYPE_RITUAL,tp,tp,true,false,POS_FACEUP)
	c:SetMaterial(Group.FromCards(c))
	Duel.SpecialSummonComplete()
	c:CompleteProcedure()
end

---------------------------------------------------------------
-- [Efeito 3] – Mover para Zona de Pêndulo
---------------------------------------------------------------
function s.moveptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.CheckLocation(tp,LOCATION_PZONE,0) or Duel.CheckLocation(tp,LOCATION_PZONE,1)
	end
end

function s.movepop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) or not c:IsControler(tp) then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
	local zone=0
	if Duel.CheckLocation(tp,LOCATION_PZONE,0) then zone=0x1
	else zone=0x2 end
	Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true,zone)
end
