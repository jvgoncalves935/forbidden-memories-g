--Bob, O Construtor
local s,id=GetID()
function s.initial_effect(c)
	--Permitir atributo Pêndulo
	aux.EnablePendulumAttribute(c)
	--Permitir Pendulum Summon mesmo sendo Xyz
	--c.pendulum_type_allowed=true

	--Xyz Summon
	aux.AddXyzProcedureLevelFree(c,s.mfilter,s.xyzcheck,3,3)
	c:EnableReviveLimit()

	-----------------------
	-- (1) Boost de ATK permanente
	-----------------------
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCountLimit(1)
	e1:SetOperation(s.atkop)
	c:RegisterEffect(e1)

	-----------------------
	-- (2) Resposta a Spell (Efeito Rápido)
	-----------------------
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_DESTROY)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_CHAINING)
	e2:SetRange(LOCATION_MZONE)
	e2:SetCountLimit(1,id)
	e2:SetCondition(s.negcon)
	e2:SetCost(s.negcost)
	e2:SetTarget(s.pentg)
	e2:SetOperation(s.penop)
	c:RegisterEffect(e2)

	-----------------------
	-- (3) Efeito Pêndulo
	-----------------------
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetCategory(CATEGORY_DESTROY)
	e3:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_PHASE+PHASE_STANDBY)
	e3:SetRange(LOCATION_PZONE)
	e3:SetCountLimit(1,{id,2})
	e3:SetCondition(s.pencon)
	e3:SetTarget(s.pendesttg)
	e3:SetOperation(s.pendestop)
	c:RegisterEffect(e3)

	-----------------------
	-- (4) Turn Counter (para o efeito Pêndulo)
	-----------------------
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
	e4:SetCode(EVENT_MOVE)
	e4:SetOperation(s.reset_counter)
	c:RegisterEffect(e4)
end

--Treat as Level 8 for valid Pendulum Summon
c69115024.pendulum_level=8

------------------------------------------------------------
-- (A) Materiais Xyz (3 monstros "Universo G" de níveis diferentes)
------------------------------------------------------------
function s.mfilter(c,xyzc)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_MONSTER)
end
function s.xyzcheck(g,lc,tp)
	if g:GetCount()~=3 then return false end
	local lvls={}
	for tc in aux.Next(g) do
		local lv=tc:GetLevel()
		if lv<=0 then return false end
		if lvls[lv] then return false end
		lvls[lv]=true
	end
	return true
end

------------------------------------------------------------
-- (1) Boost de ATK permanente (+300)
------------------------------------------------------------
function s.atkop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,0,nil)
	for tc in aux.Next(g) do
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_UPDATE_ATTACK)
		e1:SetValue(300)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD_DISABLE)
		tc:RegisterEffect(e1)
	end
end

------------------------------------------------------------
-- (2) Efeito Rápido: oponente ativa uma Magia
------------------------------------------------------------
function s.negcon(e,tp,eg,ep,ev,re,r,rp)
	return rp==1-tp and re:IsActiveType(TYPE_SPELL)
end
function s.negcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():CheckRemoveOverlayCard(tp,3,REASON_COST) end
	e:GetHandler():RemoveOverlayCard(tp,3,3,REASON_COST)
end
function s.pentg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(aux.TRUE,tp,LOCATION_PZONE,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,tp,LOCATION_PZONE)
end
function s.penop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
	local g=Duel.SelectMatchingCard(tp,aux.TRUE,tp,LOCATION_PZONE,0,1,1,nil)
	if #g>0 and Duel.Destroy(g,REASON_EFFECT)>0 then
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		-- Impede o oponente de ativar Magias até o final do turno
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_FIELD)
		e1:SetCode(EFFECT_CANNOT_ACTIVATE)
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
		e1:SetTargetRange(0,1)
		e1:SetValue(function(e,re,tp) return re:IsActiveType(TYPE_SPELL) end)
		e1:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e1,tp)
	end
end

------------------------------------------------------------
-- (3) Efeito Pêndulo: após 2 turnos, destrói-se e move 1 Pêndulo "Universo G" do GY para a PZone
------------------------------------------------------------
function s.reset_counter(e,tp,eg,ep,ev,re,r,rp)
	if e:GetHandler():IsLocation(LOCATION_PZONE) then
		e:GetHandler():SetTurnCounter(0)
	end
end

function s.pencon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsLocation(LOCATION_PZONE) then return false end
	c:SetTurnCounter(c:GetTurnCounter()+1)
	return c:GetTurnCounter()>=2
end

function s.pendesttg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,e:GetHandler(),1,0,0)
end

function s.pendestop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	-- Destrói o próprio card e garante envio para o Extra Deck face-up
	if Duel.Destroy(c,REASON_EFFECT+REASON_DESTROY)>0 then
		if not c:IsLocation(LOCATION_EXTRA) then
			Duel.SendtoExtraP(c,tp,REASON_EFFECT)
		end

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
		local g=Duel.SelectMatchingCard(tp,s.pendfilter,tp,LOCATION_GRAVE,0,1,1,nil)
		if #g>0 then
			Duel.MoveToField(g:GetFirst(),tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		end
	end
end

function s.pendfilter(c)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_PENDULUM)
end
