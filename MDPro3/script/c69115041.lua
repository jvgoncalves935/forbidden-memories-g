--Buracu Negro
--69115041
local s,id=GetID()
function s.initial_effect(c)
	--Ativar (destrói todos os monstros no campo)
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_DESTROY)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCondition(s.condition)
	e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE)
	e1:SetCountLimit(1,id,EFFECT_COUNT_CODE_OATH)
	e1:SetTarget(s.target)
	e1:SetOperation(s.activate)
	e1:SetProperty(EFFECT_FLAG2_COF+EFFECT_FLAG_NO_TURN_RESET)
	c:RegisterEffect(e1)
end

--Condição: se o jogador possuir pelo menos 1 monstro no campo
function s.condition(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local p=c:GetControler()
	return Duel.IsExistingMatchingCard(Card.IsType,p,LOCATION_MZONE,0,1,nil,TYPE_MONSTER)
end

--Seleciona todos os monstros no campo para destruição
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
	-- Impede qualquer resposta até o final da chain
	if e:IsHasType(EFFECT_TYPE_ACTIVATE) then
		Duel.SetChainLimitTillChainEnd(aux.FALSE)
	end

	local g=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	if chk==0 then return #g>0 end

	Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,#g,0,0)
end

--Destrói todos os monstros no campo
function s.activate(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	if #g>0 then
		Duel.Destroy(g,REASON_EFFECT)
	end
end
