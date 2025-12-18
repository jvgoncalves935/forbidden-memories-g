--Petit Dragon fodase kkkkkkk
local s,id,o=GetID()
function s.initial_effect(c)
	-- Continuous ATK boost
	-- If you have 20+ "Universo G" cards in your Deck,
	-- Dragon monsters you control gain 6000 ATK
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_UPDATE_ATTACK)
	e1:SetRange(LOCATION_MZONE)
	e1:SetTargetRange(LOCATION_MZONE,0)
	e1:SetTarget(s.atktg)
	e1:SetCondition(s.atkcon)
	e1:SetValue(6000)
	c:RegisterEffect(e1)
	
	-- Continuous ATK boost
	-- If you have 20+ "Universo G" cards in your Deck,
	-- Dragon monsters you control gain 6000 DEF
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_UPDATE_DEFENSE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetTargetRange(LOCATION_MZONE,0)
	e2:SetTarget(s.atktg)
	e2:SetCondition(s.atkcon)
	e2:SetValue(6000)
	c:RegisterEffect(e2)
end

function s.atkcon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.GetMatchingGroupCount(
		Card.IsSetCard,tp,LOCATION_DECK,0,nil,0xc50
	)>=20
end

function s.atktg(e,c)
	return c:IsRace(RACE_DRAGON)
end
