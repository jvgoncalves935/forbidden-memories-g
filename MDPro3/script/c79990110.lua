--Orichalcos Fragma
local s,id=GetID()
function s.initial_effect(c)
  --Activate
  local e1=Effect.CreateEffect(c)
  e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
  e1:SetType(EFFECT_TYPE_ACTIVATE)
  e1:SetCode(EVENT_ATTACK_ANNOUNCE)
  e1:SetCondition(s.condition)
  e1:SetTarget(s.target)
  e1:SetOperation(s.activate)
  c:RegisterEffect(e1)
end
function s.condition(e,tp,eg,ep,ev,re,r,rp)
  local at=Duel.GetAttacker()
  return at:GetControler()~=tp
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
  if chkc then return chkc:IsLocation(LOCATION_MZONE) end
  if chk==0 then return Duel.IsExistingTarget(nil,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil) end
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
  Duel.SelectTarget(tp,nil,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
end
function s.activate(e,tp,eg,ep,ev,re,r,rp)
  local tc=Duel.GetFirstTarget()
  if tc:IsRelateToEffect(e) and tc:IsFaceup() and tc:IsType(TYPE_MONSTER) then
  local fid=e:GetHandler():GetFieldID()
  local e1=Effect.CreateEffect(e:GetHandler())
  e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F)
  e1:SetCode(EVENT_PHASE+PHASE_END)
  e1:SetCountLimit(1)
  e1:SetLabelObject(tc)
  e1:SetValue(fid)
  e1:SetReset(RESET_EVENT+0x1fe0000+RESET_PHASE+PHASE_END)
  e1:SetCondition(s.bancon)
  e1:SetOperation(s.banop)
  Duel.RegisterEffect(e1,tp)
  tc:RegisterFlagEffect(79990110,RESET_EVENT+0x1fe0000,0,1,fid)
  local e2=Effect.CreateEffect(e:GetHandler())
  e2:SetType(EFFECT_TYPE_SINGLE)
  e2:SetCode(EFFECT_INDESTRUCTABLE_BATTLE)
  e2:SetValue(1)
  e2:SetReset(RESET_EVENT+0x1fe0000+RESET_PHASE+PHASE_END)
  tc:RegisterEffect(e2)
  end
end
function s.banfilter(c)
  return c:IsFaceup() and c:IsAbleToRemove()
end
function s.filter(c)
	return c:IsCode(48179391) and c:IsFaceup()
end
function s.bancon(e,tp,eg,ep,ev,re,r,rp)
  return Duel.IsExistingTarget(s.banfilter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,nil) and Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_ONFIELD,0,1,nil)
end
function s.banop(e,tp,eg,ep,ev,re,r,rp)
  local tc=e:GetLabelObject()
  if tc:GetFlagEffectLabel(79990110)==e:GetValue() then
  local rg=Duel.GetMatchingGroup(s.banfilter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,nil)
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
  local srg=rg:Select(tp,1,1,nil)
  Duel.Remove(srg,POS_FACEUP,REASON_EFFECT)
  end
end