--Alemão (Arnold)
local s,id=GetID()
function s.initial_effect(c)
	--Permitir atributo Pêndulo
	aux.EnablePendulumAttribute(c)

	--Xyz Summon
	aux.AddXyzProcedureLevelFree(c,s.mfilter,s.xyzcheck,3,3)
	c:EnableReviveLimit()

	-- (2) Resposta a Trap (Efeito Rápido)
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

	-- Não pode ser destruído por batalha
	local e5=Effect.CreateEffect(c)
	e5:SetType(EFFECT_TYPE_SINGLE)
	e5:SetCode(EFFECT_INDESTRUCTABLE_BATTLE)
	e5:SetValue(1)
	c:RegisterEffect(e5)

	-- Você não sofre dano de batalhas envolvendo este card
	local e6=Effect.CreateEffect(c)
	e6:SetType(EFFECT_TYPE_SINGLE)
	e6:SetCode(EFFECT_AVOID_BATTLE_DAMAGE)
	e6:SetValue(1)
	c:RegisterEffect(e6)

	local e7=Effect.CreateEffect(c)
	e7:SetDescription(aux.Stringid(id,3))
	e7:SetCategory(CATEGORY_CONTROL+CATEGORY_DAMAGE)
	e7:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e7:SetCode(EVENT_DAMAGE_STEP_END)
	e7:SetProperty(EFFECT_FLAG_DELAY)
	e7:SetCondition(s.ctcon)
	e7:SetOperation(s.ctop)
	c:RegisterEffect(e7)

	local e8=Effect.CreateEffect(c)
	e8:SetDescription(aux.Stringid(id,4))
	e8:SetCategory(CATEGORY_ATTACH)
	e8:SetType(EFFECT_TYPE_QUICK_O)
	e8:SetCode(EVENT_FREE_CHAIN)
	e8:SetRange(LOCATION_PZONE)
	e8:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e8:SetCountLimit(1,id+200)
	e8:SetTarget(s.xyzattachtg)
	e8:SetOperation(s.xyzattachop)
	c:RegisterEffect(e8)

end

--Treat as Level 8 for valid Pendulum Summon
c69115050.pendulum_level=8

-- (A) Materiais Xyz (3 monstros "Universo G" de níveis diferentes)
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

-- (2) Efeito Rápido: oponente ativa uma Trap
function s.negcon(e,tp,eg,ep,ev,re,r,rp)
	return rp==1-tp
		and re:IsActiveType(TYPE_TRAP)
		and Duel.IsChainDisablable(ev)
end

function s.negcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():CheckRemoveOverlayCard(tp,3,REASON_COST) end
	e:GetHandler():RemoveOverlayCard(tp,3,3,REASON_COST)
end

function s.pentg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,0,tp,LOCATION_PZONE)
end

function s.locktrap(e,tp)
	local c=e:GetHandler()
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_CANNOT_ACTIVATE)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e1:SetTargetRange(0,1)
	e1:SetValue(function(e,re,rp)
		return rp~=tp and re:IsActiveType(TYPE_TRAP)
	end)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)
end

function s.penop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	local pz=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_PZONE,0,nil)
	local ct=#pz

	-- CASO C: 2 cards nas PZones (destruição obrigatória)
	if ct>=2 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
		local dg=pz:Select(tp,1,1,nil)
		local dc=dg:GetFirst()
		local seq=dc:GetSequence()
		if Duel.Destroy(dc,REASON_EFFECT)>0
			and Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true,1<<seq) then
			s.locktrap(e,tp)
		end
		return
	end

	-- CASO B: 1 card na PZone (destruição opcional)
	if ct==1 then
		local dc=pz:GetFirst()
		if Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
			local seq=dc:GetSequence()
			if Duel.Destroy(dc,REASON_EFFECT)>0
				and Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true,1<<seq) then
				s.locktrap(e,tp)
				return
			end
		end
		-- Não destruiu → escolhe zona livre
		if Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true) then
			s.locktrap(e,tp)
		end
		return
	end

	-- CASO A: nenhuma PZone ocupada
	if Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true) then
		s.locktrap(e,tp)
	end
end

function s.ctcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local bc=c:GetBattleTarget()
	return bc
		and bc:IsRelateToBattle()
		and bc:IsControler(1-tp)
end

function s.ctop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local bc=c:GetBattleTarget()
	if not bc or not bc:IsRelateToBattle() then return end

	-- tenta tomar controle
	Duel.GetControl(bc,tp)

	-- se continuar com o oponente, causa dano
	if bc:IsControler(1-tp) then
		local atk=math.max(bc:GetAttack(),0)
		local def=math.max(bc:GetDefense(),0)
		Duel.Damage(1-tp,atk+def,REASON_EFFECT)
	end
end

function s.xyzfilter(c)
	return c:IsFaceup()
		and c:IsSetCard(0xc50)
		and c:IsType(TYPE_XYZ)
end

function s.matfilter(c,tp)
	return
		-- 1) Qualquer card no SEU cemitério
		(c:IsLocation(LOCATION_GRAVE) and c:GetOwner()==tp)
		or
		-- 2) Armadilha com face para cima no campo do OPONENTE
		(c:IsType(TYPE_TRAP)
			and c:IsFaceup()
			and c:IsLocation(LOCATION_ONFIELD)
			and c:IsControler(1-tp))
		or
		-- 3) Armadilha no cemitério do OPONENTE
		(c:IsType(TYPE_TRAP)
			and c:IsLocation(LOCATION_GRAVE)
			and c:GetOwner()==1-tp)
end

function s.xyzattachtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(
			s.xyzfilter,tp,LOCATION_MZONE,0,1,nil
		)
		and Duel.IsExistingMatchingCard(
			s.matfilter,tp,
			LOCATION_GRAVE+LOCATION_ONFIELD,
			LOCATION_GRAVE+LOCATION_ONFIELD,
			1,nil,tp
		)
	end
end


function s.xyzattachop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local xyz=Duel.SelectMatchingCard(
		tp,s.xyzfilter,tp,LOCATION_MZONE,0,1,1,nil
	):GetFirst()
	if not xyz then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local mat=Duel.SelectMatchingCard(
		tp,s.matfilter,tp,
		LOCATION_GRAVE+LOCATION_ONFIELD,
		LOCATION_GRAVE+LOCATION_ONFIELD,
		1,1,nil,tp
	):GetFirst()
	if not mat then return end

	Duel.Overlay(xyz,Group.FromCards(mat))
end


