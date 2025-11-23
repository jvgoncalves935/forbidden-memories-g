--Twin Bow Centaur
function c79990130.initial_effect(c)
  --Activate
  local e1=Effect.CreateEffect(c)
  e1:SetType(EFFECT_TYPE_ACTIVATE)
  e1:SetCode(EVENT_FREE_CHAIN)
  c:RegisterEffect(e1)
  local e2=Effect.CreateEffect(c)
  e2:SetType(EFFECT_TYPE_IGNITION)
  e2:SetRange(LOCATION_SZONE)
  e2:SetCountLimit(1)
  e2:SetCondition(c79990130.condition)
  e2:SetCost(c79990130.cost)
  e2:SetTarget(c79990130.target)
  e2:SetOperation(c79990130.operation)
  c:RegisterEffect(e2)
end
function c79990130.condition(e,tp,eg,ep,ev,re,r,rp)
  return Duel.GetCurrentPhase()==PHASE_MAIN1
end
function c79990130.cost(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return Duel.GetActivityCount(tp,ACTIVITY_BATTLE_PHASE)==0 end
  local e1=Effect.CreateEffect(e:GetHandler())
  e1:SetType(EFFECT_TYPE_FIELD)
  e1:SetCode(EFFECT_CANNOT_BP)
  e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
  e1:SetTargetRange(1,0)
  e1:SetReset(RESET_PHASE+PHASE_END)
  Duel.RegisterEffect(e1,tp)
end
function c79990130.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
  if chkc then return false end
  if chk==0 then return Duel.IsExistingTarget(Card.IsFaceup,tp,0,LOCATION_MZONE,1,nil)
  and Duel.IsExistingTarget(Card.IsFaceup,tp,LOCATION_MZONE,0,1,nil)end
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_OPPO)
  local g1=Duel.SelectTarget(tp,Card.IsFaceup,tp,0,LOCATION_MZONE,1,1,nil)
  e:SetLabelObject(g1:GetFirst())
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SELF)
  Duel.SelectTarget(tp,Card.IsFaceup,tp,LOCATION_MZONE,0,1,1,nil)
end
function c79990130.operation(e,tp,eg,ep,ev,re,r,rp)
  local g=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
  local o=e:GetLabelObject()
  local s=g:GetFirst()
  if s==o then s=g:GetNext() end
  local res=Duel.TossCoin(tp,1)
  if res==1 then 
  Duel.Remove(o,POS_FACEUP,REASON_EFFECT)
  Duel.Damage(1-tp,o:GetBaseAttack(),REASON_EFFECT)
  else 
  Duel.Remove(s,POS_FACEUP,REASON_EFFECT)
  Duel.Damage(tp,s:GetBaseAttack(),REASON_EFFECT)
  end
end