--Petit Dragon fodase kkkkkkk
local s,id,o=GetID()

function s.initial_effect(c)
	-- ATK boost
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_UPDATE_ATTACK)
	e1:SetRange(LOCATION_MZONE)
	e1:SetTargetRange(LOCATION_MZONE,0)
	e1:SetTarget(s.atktg)
	e1:SetCondition(s.condition)
	e1:SetValue(6000)
	e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
	c:RegisterEffect(e1)

	-- DEF boost
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_UPDATE_DEFENSE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetTargetRange(LOCATION_MZONE,0)
	e2:SetTarget(s.atktg)
	e2:SetCondition(s.condition)
	e2:SetValue(6000)
	e2:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
	c:RegisterEffect(e2)

	--Becomes "Universo G" while on field, GY or banished
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_SINGLE)
	e3:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e3:SetCode(EFFECT_ADD_SETCODE)
	e3:SetRange(LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED)
	e3:SetValue(0xc50)
	c:RegisterEffect(e3)
end

-- Filtro para cards "Universo G"
function s.unigfilter(c)
	return c:IsSetCard(0xc50)
end

-- Condição: 6 ou mais "Universo G" no Deck Adicional
function s.condition(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(Card.IsSetCard,tp,LOCATION_EXTRA,0,nil,0xc50)
	return #g>=6
end

-- Alvo: Dragões que você controla
function s.atktg(e,c)
	return c:IsRace(RACE_DRAGON)
end
