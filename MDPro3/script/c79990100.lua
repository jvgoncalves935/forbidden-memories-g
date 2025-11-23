--Orichalcos Ypiretis
local s,id=GetID()
function s.initial_effect(c)
  --Special Summon
  local e1=Effect.CreateEffect(c)
  e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
  e1:SetType(EFFECT_TYPE_TRIGGER_O+EFFECT_TYPE_SINGLE)
  e1:SetCode(EVENT_SUMMON_SUCCESS)
  e1:SetCountLimit(1,id)
  e1:SetCondition(s.spcon)
  e1:SetTarget(s.sptg)
  e1:SetOperation(s.spop)
  c:RegisterEffect(e1)
end
function s.filter(c)
	return c:IsCode(48179391) and c:IsFaceup()
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp,c)
	return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_ONFIELD,0,1,nil)
end
function s.spfilter(c,e,tp)
  return c:IsType(TYPE_NORMAL) and c:IsSetCard(0x799) and c:GetLevel()==4 and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
  and not c:IsHasEffect(EFFECT_NECRO_VALLEY)
end
function s.thfilter(c,e,tp,code)
	return c:IsCode(code) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0 
  and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_GRAVE+LOCATION_DECK+LOCATION_HAND,0,1,nil,e,tp)end
  Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_GRAVE+LOCATION_DECK+LOCATION_HAND)
end
function s.spop(e,tp,eg,ep,ev,re,r,rp)
  local c=e:GetHandler()
  if Duel.GetLocationCount(tp,LOCATION_MZONE)<1 then return end
  Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
  local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_GRAVE+LOCATION_DECK+LOCATION_HAND,0,1,1,nil,e,tp)
  if g:GetCount()>0 then
  local tc=g:GetFirst()
  Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
  local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
  local tg=Duel.GetMatchingGroup(s.thfilter,tp,LOCATION_DECK+LOCATION_HAND,0,nil,e,tp,tc:GetOriginalCode())
  if ft<=0 or tg:GetCount()==0 or (ft>1 and tg:GetCount()>1 and Duel.IsPlayerAffectedByEffect(tp,59822133)) then return end
  Duel.SpecialSummon(tg,0,tp,tp,false,false,POS_FACEUP)
  end
  local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e2:SetTargetRange(1,0)
	e2:SetTarget(s.splimit)
	e2:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e2,tp)
end
function s.splimit(e,c,sump,sumtype,sumpos,targetp,se)
	return not c:IsSetCard(0x799) and c:IsLocation(LOCATION_EXTRA)
end