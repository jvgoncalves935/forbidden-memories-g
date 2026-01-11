--Poderoso Castiga
local s,id,o=GetID()
function s.initial_effect(c)
	-- Xyz Summon procedure (manual)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_EXTRA)
	e1:SetCondition(s.xyzcon)
	e1:SetOperation(s.xyzop)
	c:RegisterEffect(e1)

	-- When attacked in DEF, battle damage is inflicted to you
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_PIERCE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetTargetRange(0,LOCATION_MZONE)
	e2:SetTarget(s.piercetg)
	c:RegisterEffect(e2)

	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_BATTLE_DAMAGE_TO_EFFECT)
	e3:SetRange(LOCATION_MZONE)
	e3:SetTargetRange(0,LOCATION_MZONE)
	e3:SetTarget(s.piercetg)
	c:RegisterEffect(e3)
	
	-- Place 2 Universo G Pendulum Monsters in PZones
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,0))
	e4:SetType(EFFECT_TYPE_IGNITION)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCountLimit(1,id)
	e4:SetCost(s.pzcost)
	e4:SetTarget(s.pztg)
	e4:SetOperation(s.pzop)
	c:RegisterEffect(e4)

end

function s.xyzfilter(c)
	return c:IsSetCard(0xc50)
end

function s.xyzcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()

	-- Máximo de 3 Invocações-Especiais no turno
	if Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)>3 then
		return false
	end

	-- Precisa de 3 "Universo G" no campo (face-up ou face-down)
	return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(
			s.xyzfilter,tp,LOCATION_ONFIELD,0,3,nil
		)
end

function s.xyzop(e,tp,eg,ep,ev,re,r,rp,c)
	-- Seleciona 3 matérias
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local g=Duel.SelectMatchingCard(
		tp,s.xyzfilter,tp,LOCATION_ONFIELD,0,3,3,nil
	)

	c:SetMaterial(g)
	Duel.Overlay(c,g)

	-- Lock de Invocações pelo resto do turno
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_CANNOT_SUMMON)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e1:SetTargetRange(1,0)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)

	local e2=e1:Clone()
	e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	Duel.RegisterEffect(e2,tp)
end

function s.pzfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_PENDULUM)
		and c:IsLevelBelow(5)
		and not c:IsForbidden()
end

function s.pzcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckLPCost(tp,2800) end
	Duel.PayLPCost(tp,2800)
end

function s.pztg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return s.check_pzones(tp)
			and Duel.IsExistingMatchingCard(
				s.pzfilter,tp,
				LOCATION_DECK+LOCATION_HAND+LOCATION_GRAVE+LOCATION_REMOVED,
				0,2,nil
			)
	end
end

function s.check_pzones(tp)
	return Duel.GetFieldCard(tp,LOCATION_PZONE,0)==nil
		and Duel.GetFieldCard(tp,LOCATION_PZONE,1)==nil
end


function s.pzop(e,tp,eg,ep,ev,re,r,rp)
	if not s.check_pzones(tp) then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
	local g=Duel.SelectMatchingCard(
		tp,s.pzfilter,tp,
		LOCATION_DECK+LOCATION_HAND+LOCATION_GRAVE+LOCATION_REMOVED,
		0,2,2,nil
	)
	if #g<2 then return end

	local tc1=g:GetFirst()
	local tc2=g:GetNext()

	Duel.MoveToField(tc1,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
	Duel.MoveToField(tc2,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
end

function s.piercetg(e,c)
	local bc=c:GetBattleTarget()
	if not bc then return false end
	return bc==e:GetHandler()
		and bc:IsDefensePos()
end
