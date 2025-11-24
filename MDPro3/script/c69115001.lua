--Alexandre Senna
local s,id=GetID()
function s.initial_effect(c)
	--Habilita Pendulum Summon
	aux.EnablePendulumAttribute(c)

	-----------------------------------------
	-- SPECIAL SUMMON PROCEDURE (não gera chain)
	-----------------------------------------
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id,EFFECT_COUNT_CODE_OATH) -- hard OPT
	e1:SetCondition(s.spcon_proc)
	e1:SetTarget(s.sptg_proc)
	c:RegisterEffect(e1)

	-----------------------------------------
	-- QUICK Effect para turno do oponente (EVENT_FREE_CHAIN)
	-- Permite tentar Special Summon a partir da mão como quick
	-----------------------------------------
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetRange(LOCATION_HAND)
	e2:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE)
	e2:SetCountLimit(1,id,EFFECT_COUNT_CODE_OATH) -- compartilhar hard OPT com a procedure
	e2:SetCondition(s.spcon_quick)
	e2:SetTarget(s.sptg_quick)
	e2:SetOperation(s.spop_quick)
	c:RegisterEffect(e2)

	-----------------------------------------
	-- ATAQUE RESTRITO
	-----------------------------------------
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_ONLY_ATTACK_MONSTER)
	e3:SetRange(LOCATION_MZONE)
	e3:SetTargetRange(0,LOCATION_MZONE)
	e3:SetValue(s.atklimit)
	c:RegisterEffect(e3)

	-----------------------------------------
	-- QUICK EFFECT: quando o oponente ativa um card/efeito (EVENT_CHAINING)
	-----------------------------------------
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,2))
	e4:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e4:SetType(EFFECT_TYPE_QUICK_O)
	e4:SetCode(EVENT_CHAINING)
	e4:SetRange(LOCATION_HAND)
	e4:SetCountLimit(1,id,EFFECT_COUNT_CODE_OATH) -- mesmo hard OPT
	e4:SetCondition(s.spcon_chain)
	e4:SetTarget(s.sptg_quick)
	e4:SetOperation(s.spop_quick)
	c:RegisterEffect(e4)

end

-----------------------------------------
-- Procedure: permite invocation no próprio turno OU no turno do oponente
-- usada pelo EFFECT_SPSUMMON_PROC
-----------------------------------------
function s.spcon_proc(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
	-- pode no seu turno ou no turno do oponente (procedure aceita ambos)
	return true
end
function s.sptg_proc(e,tp,eg,ep,ev,re,r,rp,chk,c)
	return true
end

-----------------------------------------
-- Quick-condition: apenas no turno do oponente
-----------------------------------------
function s.spcon_quick(e,tp,eg,ep,ev,re,r,rp)
	-- só ativa como quick no turno do oponente
	if Duel.GetTurnPlayer()==tp then return false end
	-- precisa ter espaço e ser invocável
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
	local c=e:GetHandler()
	return c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-----------------------------------------
-- Condição: o oponente ativou card/efeito
-----------------------------------------
function s.spcon_chain(e,tp,eg,ep,ev,re,r,rp)
	-- O oponente ativou algo
	if rp==tp then return false end

	-- espaço no campo
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end

	-- pode ser invocado?
	local c=e:GetHandler()
	return c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-----------------------------------------
-- Quick target/operação (executa SpecialSummon)
-----------------------------------------
function s.sptg_quick(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.spop_quick(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	-- realiza Special Summon (como efeito/Quick)
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)~=0 then
		-- opcional: registrar flag se quiser impedir outra forma de summon no mesmo turno
		-- (mas o CountLimit compartilhado já evita que seja usado duas vezes)
	end
end

-----------------------------------------
-- RESTRIÇÃO DE ATAQUE
-----------------------------------------
function s.atklimit(e,c)
	return c==e:GetHandler()
end