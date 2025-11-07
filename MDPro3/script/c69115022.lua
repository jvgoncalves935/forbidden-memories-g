--Espanador de Penas da Harpica
--69115022
local s,id=GetID()
function s.initial_effect(c)
	--Ativação
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_DESTROY)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	-- "Uma vez por Duelo"
	e1:SetCountLimit(1,id+EFFECT_COUNT_CODE_DUEL)
	e1:SetCondition(s.condition)
	e1:SetTarget(s.target)
	e1:SetOperation(s.activate)
	c:RegisterEffect(e1)
end

--Filtro para cards "Universo G"
function s.unigfilter(c)
	return c:IsSetCard(0xc50)
end

--Condição de ativação: requer 3 ou mais cards "Universo G" na mão, campo ou cemitério (excluindo este card)
function s.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local g=Duel.GetMatchingGroup(s.unigfilter,tp,LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,c)
	return #g>=3
end

--Filtro: seleciona Magias/Armadilhas
function s.filter(c)
	return c:IsType(TYPE_SPELL+TYPE_TRAP)
end

--Target: impede respostas e declara destruição
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.filter,tp,0,LOCATION_ONFIELD,1,nil)
	end
	-- Impede qualquer resposta até o final da corrente
	if e:IsHasType(EFFECT_TYPE_ACTIVATE) then
		Duel.SetChainLimitTillChainEnd(aux.FALSE)
	end
	local sg=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_ONFIELD,nil)
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,sg,#sg,0,0)
end

--Efeito: destrói todas as Magias/Armadilhas do oponente
function s.activate(e,tp,eg,ep,ev,re,r,rp)
	local sg=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_ONFIELD,nil)
	if #sg>0 then
		Duel.Destroy(sg,REASON_EFFECT)
	end
end
