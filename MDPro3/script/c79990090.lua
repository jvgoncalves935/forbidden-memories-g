--Impact Revive
local s,id=GetID()
function s.initial_effect(c)
  --Activate
  local e1=Effect.CreateEffect(c)
  e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
  e1:SetType(EFFECT_TYPE_ACTIVATE)
  e1:SetCode(EVENT_FREE_CHAIN)
  e1:SetCountLimit(1,id+EFFECT_COUNT_CODE_OATH)
  e1:SetCondition(s.condition)
  e1:SetTarget(s.target)
  e1:SetOperation(s.activate)
  c:RegisterEffect(e1)
end
function s.filter1(c,e,tp,tid)
  return c:GetTurnID()==tid and c:IsReason(REASON_BATTLE) and c:IsCanBeSpecialSummoned(e,0,tp,true,false)
end
function s.filter2(c)
   return c:IsFaceup() and c:IsType(TYPE_MONSTER) and not c:IsHasEffect(EFFECT_EXTRA_ATTACK)
end
function s.condition(e,tp,eg,ep,ev,re,r,rp)
  return (Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and Duel.GetTurnPlayer()==tp and (Duel.GetCurrentPhase()>=PHASE_BATTLE_START and Duel.GetCurrentPhase()<=PHASE_BATTLE) 
  and Duel.IsExistingTarget(s.filter1,tp,LOCATION_GRAVE,LOCATION_GRAVE,1,nil,e,tp,Duel.GetTurnCount()) 
  and Duel.IsExistingTarget(s.filter2,tp,LOCATION_MZONE,0,1,nil)) or 
  (Duel.GetLocationCount(1-tp,LOCATION_MZONE)>0 and  Duel.GetTurnPlayer()==tp and (Duel.GetCurrentPhase()>=PHASE_BATTLE_START and Duel.GetCurrentPhase()<=PHASE_BATTLE) 
  and Duel.IsExistingTarget(s.filter1,tp,LOCATION_GRAVE,LOCATION_GRAVE,1,nil,e,tp,Duel.GetTurnCount()) 
  and Duel.IsExistingTarget(s.filter2,tp,LOCATION_MZONE,0,1,nil))
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
  if chkc then return chkc:IsLocation(LOCATION_GRAVE) and s.filter1(chkc,e,tp) end
  if chk==0 then return true end
  if Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and Duel.GetLocationCount(1-tp,LOCATION_MZONE)>0 then
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
  local g=Duel.SelectTarget(tp,s.filter1,tp,LOCATION_GRAVE,LOCATION_GRAVE,1,1,nil,e,tp,Duel.GetTurnCount())
  elseif Duel.GetLocationCount(tp,LOCATION_MZONE)>0 and Duel.GetLocationCount(1-tp,LOCATION_MZONE)<1 then
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
  local g=Duel.SelectTarget(tp,s.filter1,tp,LOCATION_GRAVE,0,1,1,nil,e,tp,Duel.GetTurnCount())
  elseif Duel.GetLocationCount(tp,LOCATION_MZONE)<1 and Duel.GetLocationCount(1-tp,LOCATION_MZONE)>0 then
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
  local g=Duel.SelectTarget(tp,s.filter1,tp,0,LOCATION_GRAVE,1,1,nil,e,tp,Duel.GetTurnCount())
  end
  Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,g,1,0,0)
end
function s.activate(e,tp,eg,ep,ev,re,r,rp)
  local tc=Duel.GetFirstTarget()
  if tc:IsRelateToEffect(e) and Duel.SpecialSummon(tc,0,tp,tc:GetOwner(),true,false,POS_FACEUP) then
  local e1=Effect.CreateEffect(e:GetHandler())
  e1:SetType(EFFECT_TYPE_SINGLE)
  e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
  e1:SetRange(LOCATION_MZONE)
  e1:SetCode(EFFECT_UPDATE_ATTACK)
  e1:SetValue(500)
  e1:SetReset(RESET_EVENT+0x1fe0000)
  tc:RegisterEffect(e1)
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
  local g=Duel.SelectMatchingCard(tp,s.filter2,tp,LOCATION_MZONE,0,1,1,nil)
  local tc2=g:GetFirst()
  Duel.HintSelection(g)
  local e2=Effect.CreateEffect(e:GetHandler())
  e2:SetType(EFFECT_TYPE_SINGLE)
  e2:SetCode(EFFECT_EXTRA_ATTACK)
  e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
  e2:SetValue(1)
  e2:SetReset(RESET_EVENT+0x1fe0000+RESET_PHASE+PHASE_END)
  tc2:RegisterEffect(e2)
  end
end