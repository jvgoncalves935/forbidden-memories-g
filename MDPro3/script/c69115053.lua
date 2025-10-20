--Sarcófago da Ícaro Studios
--c69115050
local s,id=GetID()
function s.initial_effect(c)
	------------------------------
	-- (1) Ativar + Buscar monstro Universo G
	------------------------------
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetTarget(s.thtg)
	e1:SetOperation(s.thop)
	c:RegisterEffect(e1)
	------------------------------
	-- (2) Permitir ativar Magias-Rápidas Universo G da mão no turno do oponente
	------------------------------
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_QP_ACT_IN_NTPHAND)
	e2:SetRange(LOCATION_FZONE)
	e2:SetTargetRange(LOCATION_HAND,0)
	e2:SetCondition(s.qpcon)
	e2:SetTarget(aux.TargetBoolFunction(Card.IsSetCard,0xc50))
	c:RegisterEffect(e2)
	------------------------------
	-- (3) Reciclar até 2 cards do Cemitério e comprar o mesmo número
	------------------------------
	local e3=Effect.CreateEffect(c)
	e3:SetCategory(CATEGORY_TODECK+CATEGORY_DRAW)
	e3:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_CHAINING)
	e3:SetProperty(EFFECT_FLAG_DELAY+EFFECT_FLAG_CARD_TARGET)
	e3:SetRange(LOCATION_FZONE)
	e3:SetCountLimit(1,id)
	e3:SetCondition(s.tdcon)
	e3:SetTarget(s.tdtg)
	e3:SetOperation(s.tdop)
	c:RegisterEffect(e3)
end

---------------------------------------
-- Função (1): Buscar monstro Universo G
---------------------------------------
function s.thfilter(c)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_MONSTER) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_SEARCH,nil,1,tp,LOCATION_DECK)
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

---------------------------------------------------
-- Função (2): Condição para ativar Magias-Rápidas na mão
---------------------------------------------------
function s.qpcon(e,tp,eg,ep,ev,re,r,rp)
	-- Se o jogador controla ou tem na mão QUALQUER card do arquétipo Universo G (exceto este card)
	return Duel.IsExistingMatchingCard(s.qpcondfilter,tp,LOCATION_HAND+LOCATION_ONFIELD,0,1,e:GetHandler())
end
function s.qpcondfilter(c)
	return c:IsSetCard(0xc50)
end

---------------------------------------------------
-- Função (3): Reciclar e Comprar
---------------------------------------------------
function s.tdcon(e,tp,eg,ep,ev,re,r,rp)
	-- Verifica se você ativou uma Magia-Rápida Universo G da mão
	local rc=re:GetHandler()
	return rp==tp and re:IsActiveType(TYPE_SPELL) and re:IsActiveType(TYPE_QUICKPLAY)
		and re:IsHasType(EFFECT_TYPE_ACTIVATE) and rc:IsSetCard(0xc50) and re:GetActivateLocation()==LOCATION_HAND
end
function s.tdfilter(c)
	return c:IsSetCard(0xc50) and c:IsAbleToDeck()
end
function s.tdtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_GRAVE) and chkc:IsControler(tp) and s.tdfilter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(s.tdfilter,tp,LOCATION_GRAVE,0,1,nil)
		and Duel.IsPlayerCanDraw(tp) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local g=Duel.SelectTarget(tp,s.tdfilter,tp,LOCATION_GRAVE,0,1,2,nil)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,g,#g,0,0)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,#g)
end
function s.tdop(e,tp,eg,ep,ev,re,r,rp)
	local sg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)
	if #sg==0 then return end
	Duel.SendtoDeck(sg,nil,SEQ_DECKBOTTOM,REASON_EFFECT)
	local og=Duel.GetOperatedGroup()
	local ct=og:FilterCount(Card.IsLocation,nil,LOCATION_DECK)
	if ct>0 then
		Duel.BreakEffect()
		Duel.Draw(tp,ct,REASON_EFFECT)
	end
end
