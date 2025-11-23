--Orichalcos Gigas
local s,id=GetID()
function s.initial_effect(c)
  --Special Summon + 500 ATK
  local e1=Effect.CreateEffect(c)
  e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
  e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
  e1:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DELAY)
  e1:SetCode(EVENT_TO_GRAVE)
  e1:SetCondition(s.condition)
  e1:SetTarget(s.target)
  e1:SetOperation(s.operation)
  c:RegisterEffect(e1)
	
  if not s.global_check then
  s.global_check=true
  s[0]=0
  s[1]=0
  local ge1=Effect.CreateEffect(c)
  ge1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
  ge1:SetCode(EVENT_DESTROYED)
  ge1:SetOperation(s.checkop)
  Duel.RegisterEffect(ge1,0)
end
end
function s.condition(e,tp,eg,ep,ev,re,r,rp)
  return e:GetHandler():IsReason(REASON_DESTROY)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
  and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false) end
  Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
end
function s.operation(e,tp,eg,ep,ev,re,r,rp)
  if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
  if e:GetHandler() then
  Duel.SpecialSummon(e:GetHandler(),0,tp,tp,false,false,POS_FACEUP)
  local e1=Effect.CreateEffect(e:GetHandler())
  e1:SetType(EFFECT_TYPE_FIELD)
  e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
  e1:SetCode(EFFECT_SKIP_DP)
  e1:SetTargetRange(1,0)
  e1:SetReset(RESET_PHASE+PHASE_END,3)
  Duel.RegisterEffect(e1,tp)
  --+500 Every time destroyed
  local e2=Effect.CreateEffect(e:GetHandler())
  e2:SetType(EFFECT_TYPE_SINGLE)
  e2:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
  e2:SetRange(LOCATION_MZONE)
  e2:SetCode(EFFECT_UPDATE_ATTACK)
  e2:SetValue(s[tp]+500)
  e:GetHandler():RegisterEffect(e2)
  e:GetHandler():CompleteProcedure()
  end
end
function s.checkop(e,tp,eg,ep,ev,re,r,rp)
  s[ep]=s[ep]
end