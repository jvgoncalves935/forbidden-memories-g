--Orichalcos Dexia
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
  --ATK Increase
  local e4=Effect.CreateEffect(c)
  e4:SetType(EFFECT_TYPE_SINGLE)
  e4:SetCode(EFFECT_SET_ATTACK_FINAL)
  e4:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
  e4:SetRange(LOCATION_MZONE)
  e4:SetCondition(s.atkcon)
  e4:SetValue(s.atkval)
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
function s.atkcon(e)
	return Duel.GetCurrentPhase()==PHASE_DAMAGE_CAL and e:GetHandler():GetBattleTarget()
end
function s.atkval(e,c)
  local ph=Duel.GetCurrentPhase()
  local c=e:GetHandler()
  local a=Duel.GetAttacker()
  local d=Duel.GetAttackTarget()
  if d==nil then return end
  if ph==PHASE_DAMAGE_CAL or PHASE_DAMAGE or Duel.IsDamageCalculated() and c:IsRelateToBattle() then
  if a==c and d:IsAttackPos() then return d:GetAttack()+300 end
  if a==c and d:IsDefensePos() then return d:GetDefense()+300 end
  if d==c then return a:GetAttack()+300 end
  if not a==c and not d==c then return 0 end
  end
  if not ph==PHASE_DAMAGE_CAL or not PHASE_DAMAGE or not Duel.IsDamageCalculated() then return 0 end
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
  e1:SetValue(-e:GetHandler():GetAttack())
  e1:SetReset(RESET_EVENT+0x1fe0000)
  tc:RegisterEffect(e1)
  end
end
function s.descon(e)
  return not Duel.IsExistingMatchingCard(s.filter1,e:GetHandlerPlayer(),LOCATION_MZONE,0,1,nil)
end