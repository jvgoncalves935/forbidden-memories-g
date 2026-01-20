-- Maldita Hora Que Eu Sentei Nesse Banco
local s,id=GetID()

function s.initial_effect(c)

	-- Ativar
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCountLimit(1,id) -- hard once per turn
	e1:SetCondition(s.actcon)
	e1:SetTarget(s.acttg)
	e1:SetOperation(s.actop)
	c:RegisterEffect(e1)

	-- Ativar da mão no turno do oponente se não controla cards
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_QP_ACT_IN_NTPHAND)
	e2:SetCondition(s.handcon)
	c:RegisterEffect(e2)

end

-- Condição para ativar da mão no turno do oponente
function s.handcon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.GetTurnPlayer()~=tp
		and Duel.GetFieldGroupCount(tp,LOCATION_ONFIELD,0)==0
end

-- Condição geral de ativação (evita ativar sem 3 alvos)
function s.actcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,3,nil)
end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SPELL+TYPE_TRAP)
		and c:IsAbleToHand()
end

function s.acttg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,3,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.actop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK,0,3,3,nil)
	if #g<3 then return end

	-- Revela os 3 cards
	Duel.ConfirmCards(1-tp,g)

	-- Embaralha e o oponente escolhe 1 aleatoriamente
	local sg=g:RandomSelect(1-tp,1)
	local tc=sg:GetFirst()

	-- Adiciona à mão
	Duel.SendtoHand(tc,nil,REASON_EFFECT)
	Duel.ConfirmCards(tp,tc)

	-- Devolve o resto ao deck e embaralha
	g:RemoveCard(tc)
	Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
end
