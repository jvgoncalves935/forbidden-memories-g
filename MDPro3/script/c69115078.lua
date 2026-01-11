-- Jô Abdul
local s,id=GetID()
function s.initial_effect(c)
	-- Pendulum Summon enable
	aux.EnablePendulumAttribute(c)

	-- Extra Pendulum Summon (Universo G)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetRange(LOCATION_PZONE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetHintTiming(0,TIMING_MAIN_END)
	e1:SetCountLimit(1,id) -- hard OPT
	e1:SetOperation(s.pendop)
	c:RegisterEffect(e1)

	-- End Phase (Start): draw 1, banish this card face-down
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,2))
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F)
	e2:SetCode(EVENT_PHASE+PHASE_END)
	e2:SetRange(LOCATION_PZONE)
	e2:SetCountLimit(1,id+200)
	e2:SetOperation(s.epop)
	c:RegisterEffect(e2)

	-- Can attack while in Defense Position
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_SINGLE)
	e3:SetCode(EFFECT_DEFENSE_ATTACK)
	e3:SetValue(1)
	c:RegisterEffect(e3)

		-- Special Summon itself if any card is destroyed or banished
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,3))
	e4:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCode(EVENT_DESTROYED)
	e4:SetRange(LOCATION_HAND+LOCATION_EXTRA)
	e4:SetCountLimit(1,id+300)
	e4:SetCondition(s.spcon)
	e4:SetTarget(s.sptg)
	e4:SetOperation(s.spop)
	c:RegisterEffect(e4)

	local e5=e4:Clone()
	e5:SetCode(EVENT_REMOVE)
	c:RegisterEffect(e5)

end

function s.pendop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	-- Segurança adicional (engine padrão)
	if Duel.GetFlagEffect(tp,id)~=0 then return end

	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,1))
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_EXTRA_PENDULUM_SUMMON)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e1:SetTargetRange(1,0)
	e1:SetCountLimit(1,id+100)
	e1:SetValue(s.pendvalue)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)

	Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
end

function s.pendvalue(e,c)
	return c:IsSetCard(0xc50)
end

function s.epop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	Duel.Draw(tp,1,REASON_EFFECT)
	Duel.Remove(c,POS_FACEDOWN,REASON_EFFECT)
end

function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:IsLocation(LOCATION_EXTRA) and not c:IsFaceup() then
		return false
	end
	return true
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end
