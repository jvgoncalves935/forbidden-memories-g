--Chorão, O Viajante de Mundos Paralelos
--69115017
local s,id=GetID()
function s.initial_effect(c)
	-- Permitir Invocação-Pêndulo
	aux.EnablePendulumAttribute(c)

	--------------------------------------------------------------
	-- [Efeito 1] (Mão) Efeito Rápido: Envia 1 do Deck, compra 1, retorna 1
	--------------------------------------------------------------
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOGRAVE+CATEGORY_DRAW)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.handcon)
	e1:SetTarget(s.handtg)
	e1:SetOperation(s.handop)
	c:RegisterEffect(e1)

	--------------------------------------------------------------
	-- [Efeito 2] (Campo/Cemitério) Recuperar Magia Normal "Universo G"
	--------------------------------------------------------------
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_TOHAND)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	e2:SetCountLimit(1,id+100)
	e2:SetTarget(s.thtg)
	e2:SetOperation(s.thop)
	c:RegisterEffect(e2)
	local e3=e2:Clone()
	e3:SetCode(EVENT_TO_GRAVE)
	c:RegisterEffect(e3)
end

--------------------------------------------------------------
-- [Efeito 1] (Mão) Efeito Rápido
--------------------------------------------------------------
-- Condição: você deve controlar/ter na mão ou Cemitério 1 card "Universo G"
function s.universefilter(c)
	return c:IsSetCard(0xc50)
end
function s.handcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsExistingMatchingCard(s.universefilter,tp,LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,1,nil)
end

function s.tgfilter(c)
	return c:IsAbleToGrave()
end
function s.handtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsPlayerCanDraw(tp,1)
			and Duel.IsExistingMatchingCard(s.tgfilter,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,nil,1,tp,LOCATION_DECK)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.handop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local g=Duel.SelectMatchingCard(tp,s.tgfilter,tp,LOCATION_DECK,0,1,1,nil)
	if #g>0 and Duel.SendtoGrave(g,REASON_EFFECT)>0 and Duel.Draw(tp,1,REASON_EFFECT)>0 then
		Duel.ShuffleHand(tp)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
		local hg=Duel.SelectMatchingCard(tp,Card.IsAbleToDeck,tp,LOCATION_HAND,0,1,1,nil)
		if #hg>0 then
			Duel.SendtoDeck(hg,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
		end
	end
end

--------------------------------------------------------------
-- [Efeito 2] Recuperar Magia Normal "Universo G"
--------------------------------------------------------------
function s.thfilter(c)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_SPELL) and c:IsType(TYPE_NORMAL)
		and c:IsAbleToHand() and (c:IsLocation(LOCATION_GRAVE) or c:IsFaceup())
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_GRAVE+LOCATION_REMOVED)
end
function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
end

