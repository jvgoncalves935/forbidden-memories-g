--Pote da Ignorância
local s,id=GetID()

function s.initial_effect(c)
	Duel.AddCustomActivityCounter(id,ACTIVITY_CHAIN,s.chainfilter)

	-- Deck effect: add this card to hand
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND)
	e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_DECK)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.deckcon)
	e1:SetTarget(s.decktg)
	e1:SetOperation(s.deckop)
	c:RegisterEffect(e1)

	-- Hand effect: draw 2 (normal spell activation)
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_DRAW)
	e2:SetType(EFFECT_TYPE_ACTIVATE)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetCountLimit(1,id+200)
	e2:SetCondition(s.handcon)
	e2:SetTarget(s.handtg)
	e2:SetOperation(s.handop)
	c:RegisterEffect(e2)
end

-- Exclude non-monster effects (only count monster effect activations)
function s.chainfilter(re,tp,cid)
	return not (re:IsActiveType(TYPE_MONSTER))
end

-- Opponent activated 3+ monster effects this turn
function s.opp_activated_enough(tp)
	return Duel.GetCustomActivityCount(id,1-tp,ACTIVITY_CHAIN)>=3
end

-- Deck effect condition
function s.deckcon(e,tp,eg,ep,ev,re,r,rp)
	return s.opp_activated_enough(tp)
end

function s.decktg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsAbleToHand() end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,c,1,0,0)
end

function s.deckop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:IsLocation(LOCATION_DECK) and c:IsAbleToHand() then
		Duel.SendtoHand(c,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,c)
	end
end

-- Hand effect condition
function s.handcon(e,tp,eg,ep,ev,re,r,rp)
	return s.opp_activated_enough(tp)
end

function s.handtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,2) end
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
end

function s.handop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Draw(tp,2,REASON_EFFECT)
end
