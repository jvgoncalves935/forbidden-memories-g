--Orichalcos Kyutora
local s,id=GetID()
function s.initial_effect(c)
  --Special Summon
  local e1=Effect.CreateEffect(c)
  e1:SetType(EFFECT_TYPE_FIELD)
  e1:SetCode(EFFECT_SPSUMMON_PROC)
  e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
  e1:SetRange(LOCATION_HAND)
  e1:SetCondition(s.spcon)
  e1:SetOperation(s.spop)
  c:RegisterEffect(e1)
  --Avoid battle damage
  local e2=Effect.CreateEffect(c)
  e2:SetType(EFFECT_TYPE_FIELD)
  e2:SetCode(EFFECT_AVOID_BATTLE_DAMAGE)
  e2:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
  e2:SetRange(LOCATION_ONFIELD)
  e2:SetTargetRange(LOCATION_MZONE,0)
  e2:SetCondition(s.dmcon)
  e2:SetValue(1)
  c:RegisterEffect(e2)
  --Special Summon Shunoros
  local e3=Effect.CreateEffect(c)
  e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
  e3:SetCategory(CATEGORY_SPECIAL_SUMMON)
  e3:SetProperty(EFFECT_FLAG_DELAY)
  e3:SetCode(EVENT_DESTROYED)
  e3:SetCondition(s.spcon2)
  e3:SetTarget(s.sptg2)
  e3:SetOperation(s.spop2)
  c:RegisterEffect(e3)
end
s.listed_names={7634581,48179391}
function s.filter(c)
	return c:IsCode(48179391) and c:IsFaceup()
end
function s.spcon(e,c)
  if c==nil then return true end
  return Duel.GetLocationCount(c:GetControler(),LOCATION_MZONE)>0 and Duel.CheckLPCost(c:GetControler(),500) --Duel.IsExistingMatchingCard(s.filter,c:GetControler(),LOCATION_ONFIELD,0,1,nil)
end
function s.spop(e,tp,eg,ep,ev,re,r,rp,c)
  Duel.PayLPCost(tp,500)
end
function s.dmcon(e,tp,eg,ep,ev,re,r,rp,c)
	return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_ONFIELD,0,1,nil)
end
function s.spfilter(c,e,tp)
	return c:IsCode(7634581) and c:IsCanBeSpecialSummoned(e,0,tp,true,true)
end
function s.spcon2(e,tp,eg,ep,ev,re,r,rp,c)
	return (r&REASON_EFFECT+REASON_BATTLE)~=0 and Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_ONFIELD,0,1,nil)
end
function s.sptg2(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,e,tp) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND+LOCATION_DECK)
end
function s.spop2(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,1,nil,e,tp)
	if #g>0 then
		Duel.SpecialSummon(g,0,tp,tp,true,true,POS_FACEUP)
	end
end
