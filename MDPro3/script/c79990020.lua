--Maytr Curse
local s,id=GetID()
function s.initial_effect(c)
  local e1=Effect.CreateEffect(c)
  e1:SetType(EFFECT_TYPE_ACTIVATE)
  e1:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DELAY)
  e1:SetCode(EVENT_DESTROYED)
  e1:SetCondition(s.bacon)
  e1:SetTarget(s.batg)
  e1:SetOperation(s.baop)
  c:RegisterEffect(e1)
end
function s.bacon(e,tp,eg,ep,ev,re,r,rp)
  local ph=Duel.GetCurrentPhase()
  return eg:IsExists(s.cfilter,1,nil,tp) and Duel.GetTurnPlayer()~=tp
  and (ph==PHASE_BATTLE or ph==PHASE_DAMAGE or ph==PHASE_DAMAGE_CAL)
end
function s.cfilter(c,tp)
  return c:IsReason(REASON_BATTLE+REASON_EFFECT) and c:IsPreviousLocation(LOCATION_MZONE) and c:GetPreviousControler()==tp
end
function s.batg(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return Duel.IsExistingMatchingCard(Card.IsPosition,tp,LOCATION_MZONE,0,1,nil,POS_FACEUP_ATTACK)
  and Duel.IsExistingMatchingCard(Card.IsPosition,tp,0,LOCATION_MZONE,1,nil,POS_FACEUP_ATTACK) end
  local d=Duel.SelectTarget(tp,Card.IsPosition,tp,0,LOCATION_MZONE,1,1,nil,POS_FACEUP_ATTACK)
  local a=Duel.SelectTarget(tp,Card.IsPosition,tp,LOCATION_MZONE,0,1,1,nil,POS_FACEUP_ATTACK)
  s[0]=a:GetFirst()
  s[1]=d:GetFirst()
end
function s.baop(e,tp,eg,ep,ev,re,r,rp)
  local c=e:GetHandler()    
  local a=s[0]
  local d=s[1]
  if a:IsAttackPos() and d:IsAttackPos() then
  --cannot trigger
  local e1=Effect.CreateEffect(c)
  e1:SetType(EFFECT_TYPE_SINGLE)
  e1:SetCode(EFFECT_CANNOT_TRIGGER)
  e1:SetReset(RESET_EVENT+0x1ff0000+RESET_PHASE+PHASE_DAMAGE)
  d:RegisterEffect(e1)
  --disable
  local e2=Effect.CreateEffect(c)
  e2:SetType(EFFECT_TYPE_SINGLE)
  e2:SetCode(EFFECT_DISABLE)
  e2:SetReset(RESET_EVENT+0x1ff0000+RESET_PHASE+PHASE_DAMAGE)
  d:RegisterEffect(e2)
  Duel.CalculateDamage(d,a)
  end
end