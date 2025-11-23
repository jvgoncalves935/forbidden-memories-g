--Mirror Knight Calling
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	--Special Summon Tokens
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_TOKEN)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(s.spcon)
	e1:SetTarget(s.target)
	e1:SetOperation(s.operation)
	c:RegisterEffect(e1)
	--Renew Mirror Shields
	local e2=Effect.CreateEffect(c)
	e2:SetCategory(CATEGORY_COUNTER)
	e2:SetType(EFFECT_TYPE_TRIGGER_F+EFFECT_TYPE_FIELD)
	e2:SetRange(LOCATION_MZONE+LOCATION_SZONE)
	e2:SetCode(EVENT_PHASE+PHASE_STANDBY)
	e2:SetCountLimit(1)
	e2:SetCondition(s.rencon)
	e2:SetOperation(s.renop)
	c:RegisterEffect(e2)
end
function s.filter(c)
	return c:IsCode(48179391) and c:IsFaceup()
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
 return bit.band(e:GetHandler():GetSummonType(),SUMMON_TYPE_RITUAL)==SUMMON_TYPE_RITUAL and Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_ONFIELD,0,1,nil)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
 local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
 if chk==0 then return not Duel.IsPlayerAffectedByEffect(tp,59822133)
 and ft>0 end
 Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,ft,tp,0)
 Duel.SetOperationInfo(0,CATEGORY_TOKEN,nil,ft,tp,0)
end
function s.operation(e,tp,eg,ep,ev,re,r,rp)
 local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
 if ft<1 then return end
 if Duel.IsPlayerAffectedByEffect(tp,59822133) then ft=1 end
 if not Duel.IsPlayerCanSpecialSummonMonster(tp,79990195,0,0x799,0,0,1,RACE_WARRIOR,ATTRIBUTE_DARK) then return end
 for i=1,ft do
 local token=Duel.CreateToken(tp,79990195)
 Duel.SpecialSummonStep(token,0,tp,tp,false,false,POS_FACEUP)
 token:AddCounter(0x1106,1)
 local e1=Effect.CreateEffect(e:GetHandler())
 e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
 e1:SetCode(EFFECT_DESTROY_REPLACE)
 e1:SetTarget(s.reptg)
 e1:SetOperation(s.repop)
 e1:SetReset(RESET_EVENT+0x1fe0000)
 token:RegisterEffect(e1)
 local e2=Effect.CreateEffect(e:GetHandler())
 e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
 e2:SetCode(EVENT_PRE_DAMAGE_CALCULATE)
 e2:SetCondition(s.atkcon)
 e2:SetOperation(s.atkop)
 token:RegisterEffect(e2)
 end
 Duel.SpecialSummonComplete()
end
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
 local c=e:GetHandler()
 local bc=c:GetBattleTarget()
 return bc and bc:IsControler(1-tp) and e:GetHandler():GetCounter(0x1106)~=0
end
function s.atkop(e,tp,eg,ep,ev,re,r,rp)
 local c=e:GetHandler()
 local bc=c:GetBattleTarget()
 if c:IsRelateToBattle() and c:IsFaceup() and bc:IsRelateToBattle() and bc:IsFaceup() then
 local e1=Effect.CreateEffect(e:GetHandler())
 e1:SetType(EFFECT_TYPE_SINGLE)
 e1:SetCode(EFFECT_SET_ATTACK_FINAL)
 e1:SetReset(RESET_EVENT+0x1fe0000+RESET_PHASE+PHASE_DAMAGE)
 e1:SetValue(bc:GetAttack())
 e:GetHandler():RegisterEffect(e1)
 end
end
function s.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
 if chk==0 then return e:GetHandler():GetCounter(0x1106)>0 end
 return true
end
function s.repop(e,tp,eg,ep,ev,re,r,rp)
 e:GetHandler():RemoveCounter(tp,0x1106,1,REASON_EFFECT)
end
function s.renfilter(c)
 return c:IsCode(79990195) and c:GetCounter(0x1106)==0 
end
function s.rencon(e,tp,eg,ep,ev,re,r,rp)
 return Duel.GetTurnPlayer()==tp and Duel.IsExistingMatchingCard(s.renfilter,tp,LOCATION_MZONE,0,1,nil)
end
function s.renop(e,tp,eg,ep,ev,re,r,rp)
 if not e:GetHandler():IsRelateToEffect(e) then return end
 local g=Duel.GetMatchingGroup(Card.IsCode,tp,LOCATION_MZONE,0,nil,79990195)
 local tc=g:GetFirst()
 while tc do
 if tc:GetCounter(0x1106)==0 then
 tc:AddCounter(0x1106,1)
 end
 tc=g:GetNext()
 end
end
