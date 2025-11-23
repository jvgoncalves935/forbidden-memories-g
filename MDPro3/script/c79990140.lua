--Orichalcos Aristeros
local s,id=GetID()
function s.initial_effect(c)
  c:EnableReviveLimit()
  --cannot special summon
  local e1=Effect.CreateEffect(c)
  e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
  e1:SetType(EFFECT_TYPE_SINGLE)
  e1:SetCode(EFFECT_SPSUMMON_CONDITION)
  e1:SetValue(aux.FALSE)
  c:RegisterEffect(e1)
  --Cannot Destroy by Battle
  local e2=Effect.CreateEffect(c)
  e2:SetType(EFFECT_TYPE_SINGLE)
  e2:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
  e2:SetCode(EFFECT_INDESTRUCTABLE_BATTLE)
  e2:SetRange(LOCATION_MZONE)
  e2:SetCondition(s.condition)
  e2:SetValue(1)
  c:RegisterEffect(e2)
  --Cannot Destroy by Effect
  local e3=Effect.CreateEffect(c)
  e3:SetType(EFFECT_TYPE_SINGLE)
  e3:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
  e3:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
  e3:SetRange(LOCATION_MZONE)
  e3:SetCondition(s.condition)
  e3:SetValue(1)
  c:RegisterEffect(e3)
  --change target
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,0))
	e4:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e4:SetCode(EVENT_BE_BATTLE_TARGET)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCondition(s.cbcon)
	e4:SetOperation(s.cbop)
	c:RegisterEffect(e4)
  --Shunoros Debuf
  local e5=Effect.CreateEffect(c)
  e5:SetCategory(CATEGORY_REMOVE)
  e5:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
  e5:SetCode(EVENT_BATTLED)
  e5:SetTarget(s.target)
  e5:SetOperation(s.operation)
  c:RegisterEffect(e5)
  --Destroyed when Shunoros leaves the field
  local e6=Effect.CreateEffect(c)
  e6:SetType(EFFECT_TYPE_SINGLE)
  e6:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
  e6:SetRange(LOCATION_MZONE)
  e6:SetCode(EFFECT_SELF_DESTROY)
  e6:SetCondition(s.descon)
  c:RegisterEffect(e6)
end
function s.filter1(c)
  return c:IsFaceup() and c:IsCode(7634581) 
end
function s.condition(e)
  return Duel.IsExistingMatchingCard(s.filter1,e:GetHandlerPlayer(),LOCATION_MZONE,0,1,nil)
end
function s.cbcon(e,tp,eg,ep,ev,re,r,rp)
	local bt=eg:GetFirst()
	return r~=REASON_REPLACE and bt~=e:GetHandler() and bt:IsControler(tp) and bt:IsSetCard(0x799)
end
function s.cbop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		local at=Duel.GetAttacker()
		if at:IsAttackable() and not at:IsImmuneToEffect(e) and not c:IsImmuneToEffect(e) then
			local def=at:GetAttack()+300
			local e1=Effect.CreateEffect(c)
			e1:SetType(EFFECT_TYPE_SINGLE)
			e1:SetCode(EFFECT_SET_DEFENSE_FINAL)
			e1:SetValue(def)
			e1:SetReset(RESET_EVENT+0x1ff0000+RESET_PHASE+PHASE_DAMAGE)
			c:RegisterEffect(e1)
			Duel.CalculateDamage(at,c)
		end
	end
end
function s.filter2(c)
  return c:IsFaceup() and c:IsCode(7634581) and c:GetAttack()~=0
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
  if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(tp) and s.filter2(chkc) end
  if chk==0 then return Duel.IsExistingTarget(s.filter2,tp,LOCATION_MZONE,0,1,nil) end
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
  Duel.SelectTarget(tp,s.filter2,tp,LOCATION_MZONE,0,1,1,nil)
end
function s.operation(e,tp,eg,ep,ev,re,r,rp)
  local tc=Duel.GetFirstTarget()
  if tc:IsRelateToEffect(e) and tc:IsFaceup() then
  local e1=Effect.CreateEffect(e:GetHandler())
  e1:SetType(EFFECT_TYPE_SINGLE)
  e1:SetCode(EFFECT_UPDATE_ATTACK)
  e1:SetValue(-e:GetHandler():GetDefense())
  e1:SetReset(RESET_EVENT+0x1fe0000)
  tc:RegisterEffect(e1)
  end
end
function s.descon(e)
  return not Duel.IsExistingMatchingCard(s.filter1,e:GetHandlerPlayer(),LOCATION_MZONE,0,1,nil)
end