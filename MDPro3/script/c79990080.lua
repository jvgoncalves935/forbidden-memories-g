--Orichalcos Aspida
local s,id=GetID()
function s.initial_effect(c)
	--Summon with no tribute
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_SUMMON_PROC)
	e1:SetCondition(s.ntcon)
	c:RegisterEffect(e1)
	--To defense
	local e2=Effect.CreateEffect(c)
	e2:SetCategory(CATEGORY_POSITION)
	e2:SetType(EFFECT_TYPE_TRIGGER_F+EFFECT_TYPE_SINGLE)
	e2:SetCode(EVENT_SUMMON_SUCCESS)
	e2:SetTarget(s.potg)
	e2:SetOperation(s.poop)
	c:RegisterEffect(e2)
	--Change Battle Target
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_ATTACK_ANNOUNCE)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1)
	e3:SetCondition(s.condition)
	e3:SetOperation(s.operation)
	c:RegisterEffect(e3)
end
function s.ntfilter(c)
	return c:IsFaceup() and c:IsCode(48179391)
end
function s.ntcon(e,c,minc)
	if c==nil then return true end
	return minc==0 and c:IsLevelAbove(5) and Duel.GetLocationCount(c:GetControler(),LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.ntfilter,c:GetControler(),LOCATION_ONFIELD,0,1,nil)
end
function s.potg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
  if chk==0 then return e:GetHandler():IsAttackPos() end
  Duel.SetOperationInfo(0,CATEGORY_POSITION,e:GetHandler(),1,0,0)
end
function s.poop(e,tp,eg,ep,ev,re,r,rp)
  local c=e:GetHandler()
  if c:IsFaceup() and c:IsAttackPos() and c:IsRelateToEffect(e) then
  Duel.ChangePosition(c,POS_FACEUP_DEFENSE)
  end
end
function s.condition(e,tp,eg,ep,ev,re,r,rp)
  local at=Duel.GetAttackTarget()
  return Duel.GetTurnPlayer()~=tp and at and at:IsFaceup() and at:IsSetCard(0x799) and Duel.GetTurnPlayer()~=tp and at~=e:GetHandler()
end
function s.operation(e,tp,eg,ep,ev,re,r,rp)
  local c=e:GetHandler()
  if c:IsRelateToEffect(e) then
  local at=Duel.GetAttacker()
  if at:IsAttackable() and not at:IsImmuneToEffect(e) then
  Duel.CalculateDamage(at,c)
  end
  end
end