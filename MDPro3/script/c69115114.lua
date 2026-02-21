-- Massacote Interruptions & Faceless Games
-- 69115114
local s,id=GetID()
function s.initial_effect(c)
	-- (1) Quando Invocado: pode trocar o Nível para 3 (trigger, HOPT)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_SUMMON_SUCCESS)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCountLimit(1,id)
	e1:SetTarget(s.lvtg)
	e1:SetOperation(s.lvop)
	c:RegisterEffect(e1)
	local e1b=e1:Clone()
	e1b:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e1b)

	-- (2) Negar: add hand, Invocação-Especial, send to GY, set/place do Deck, banir do GY
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_DISABLE)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_CHAINING)
	e2:SetRange(LOCATION_HAND)
	e2:SetCountLimit(1,id+200)
	e2:SetCondition(s.discon)
	e2:SetCost(s.discost)
	e2:SetTarget(s.distg)
	e2:SetOperation(s.disop)
	c:RegisterEffect(e2)
end

-- Filtro Universo G
function s.unigfilter(c,exclude)
	return c:IsSetCard(0xc50) and (not exclude or c~=exclude)
end

-- (1) Level 3
function s.lvtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsFaceup() and e:GetHandler():GetLevel()~=3 end
end
function s.lvop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not (c:IsFaceup() and c:IsRelateToEffect(e)) then return end
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_CHANGE_LEVEL)
	e1:SetValue(3)
	e1:SetReset(RESET_EVENT+RESETS_STANDARD)
	c:RegisterEffect(e1)
end

-- (2) Condição: efeito inclui add hand / Invocação-Especial / send to GY / set ou place do Deck / banir do GY
function s.discon(e,tp,eg,ep,ev,re,r,rp)
	if not Duel.IsChainDisablable(ev) then return false end
	-- Precisa de pelo menos 2 Universo G na mão, campo e GY (exceto este card)
	local c=e:GetHandler()
	local g=Duel.GetMatchingGroup(s.unigfilter,tp,LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,c,c)
	if #g<2 then return false end

	-- Tipos de efeito que podem ser negados:
	-- Add to hand (DRAW, SEARCH, TOHAND)
	local ex4=re:IsHasCategory(CATEGORY_DRAW)
	local ex5=re:IsHasCategory(CATEGORY_SEARCH)
	local _,_,_,_,dv5=Duel.GetOperationInfo(ev,CATEGORY_TOHAND)
	local add_to_hand=ex4 or ex5 or (dv5 and bit.band(dv5,LOCATION_DECK)~=0)

	-- Special Summon (qualquer Invocação-Especial, não só do Deck)
	local ex2=Duel.GetOperationInfo(ev,CATEGORY_SPECIAL_SUMMON)
	local ss_effect=ex2

	-- Send to GY from Deck
	local ex3,_,_,_,dv3=Duel.GetOperationInfo(ev,CATEGORY_TOGRAVE)
	local send_to_gy=ex3 and dv3 and bit.band(dv3,LOCATION_DECK)~=0

	-- Set do Deck
	local ex6,_,_,_,dv6=Duel.GetOperationInfo(ev,CATEGORY_DECKDES)
	local set_from_deck=ex6 and dv6 and bit.band(dv6,LOCATION_DECK)~=0

	-- Banir do Cemitério
	local ex7,_,_,_,dv7=Duel.GetOperationInfo(ev,CATEGORY_REMOVE)
	local banish_from_gy=ex7 and dv7 and bit.band(dv7,LOCATION_GRAVE)~=0

	return add_to_hand or ss_effect or send_to_gy or set_from_deck or banish_from_gy
end

function s.discost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsDiscardable() end
	Duel.SendtoGrave(c,REASON_COST+REASON_DISCARD)
end

function s.distg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_DISABLE,eg,1,0,0)
end

function s.disop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	Duel.NegateEffect(ev)
	-- Bane este card de face para baixo (independente da negação ter sucesso)
	if c:IsLocation(LOCATION_GRAVE) then
		Duel.Remove(c,POS_FACEDOWN,REASON_EFFECT)
	end
end
