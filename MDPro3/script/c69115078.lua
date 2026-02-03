-- Jô Abdul
local s,id=GetID()
function s.initial_effect(c)
	-- Pendulum Summon enable
	aux.EnablePendulumAttribute(c)

	-- Extra Pendulum Summon (Universo G)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,3))
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

	-- Move to Pendulum Zone if any card is destroyed or banished
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,3))
	e4:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCode(EVENT_DESTROYED)
	e4:SetRange(LOCATION_HAND+LOCATION_EXTRA)
	e4:SetCountLimit(1,id+400) -- hard OPT
	e4:SetCondition(s.desban_con)
	e4:SetTarget(s.pzsptg)
	e4:SetOperation(s.pzspop)
	c:RegisterEffect(e4)

	local e5=e4:Clone()
	e5:SetCode(EVENT_REMOVE)
	c:RegisterEffect(e5)

	-- Pendulum: Special Summon itself if any card is destroyed or banished
	local e6=Effect.CreateEffect(c)
	e6:SetDescription(aux.Stringid(id,4))
	e6:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e6:SetProperty(EFFECT_FLAG_DELAY)
	e6:SetCode(EVENT_DESTROYED)
	e6:SetRange(LOCATION_PZONE)
	e6:SetCountLimit(1) -- soft once per turn
	e6:SetTarget(s.psptg)
	e6:SetOperation(s.pspop)
	e6:SetCondition(s.desban_con)
	c:RegisterEffect(e6)

	local e7=e6:Clone()
	e7:SetCode(EVENT_REMOVE)
	c:RegisterEffect(e7)

		-- If sent to GY: move to Extra Deck face-up
	local e8=Effect.CreateEffect(c)
	e8:SetDescription(aux.Stringid(id,5))
	e8:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e8:SetProperty(EFFECT_FLAG_DELAY)
	e8:SetCode(EVENT_TO_GRAVE)
	e8:SetCountLimit(1,id+600) -- hard OPT
	e8:SetTarget(s.tgextragy)
	e8:SetOperation(s.opextragy)
	c:RegisterEffect(e8)

	-- If Special Summoned by its own effect: send 1 random card from opponent's hand to GY
	local e9=Effect.CreateEffect(c)
	e9:SetDescription(aux.Stringid(id,6))
	e9:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e9:SetProperty(EFFECT_FLAG_DELAY)
	e9:SetCode(EVENT_SPSUMMON_SUCCESS)
	e9:SetCondition(s.rmdcon)
	e9:SetTarget(s.rmdtg)
	e9:SetOperation(s.rmdop)
	c:RegisterEffect(e9)

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
	e1:SetCountLimit(1,id+400)
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

function s.pzsptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetFieldCard(tp,LOCATION_PZONE,0)==nil
			or Duel.GetFieldCard(tp,LOCATION_PZONE,1)==nil
	end
end

function s.pzspop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	-- Confirma novamente se existe Zona de Pêndulo vazia
	if Duel.GetFieldCard(tp,LOCATION_PZONE,0)
		and Duel.GetFieldCard(tp,LOCATION_PZONE,1) then
		return
	end

	Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
end

function s.psptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
end

function s.pspop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end

	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end

function s.tgextragy(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return e:GetHandler():IsAbleToExtra()
	end
end

function s.opextragy(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	Duel.SendtoExtraP(c,tp,REASON_EFFECT)
end

function s.rmdcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_PZONE)
		and Duel.GetFlagEffect(tp,id+600)<2
end


function s.rmdtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetFieldGroupCount(1-tp,LOCATION_HAND,0)>0
	end
end

function s.rmdop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetFieldGroup(1-tp,LOCATION_HAND,0)
	if #g==0 then return end

	local sg=g:RandomSelect(tp,1)
	Duel.SendtoGrave(sg,REASON_EFFECT+REASON_DISCARD)

	-- conta uso por duelo
	Duel.RegisterFlagEffect(tp,id+600,0,0,1)
end

function s.desban_con(e,tp,eg,ep,ev,re,r,rp)
	-- Se for destruição, ignora batalhas
	if e:GetCode()==EVENT_DESTROYED then
		return not eg:IsExists(Card.IsReason,1,nil,REASON_BATTLE)
	end
	-- Banimento sempre é válido
	return true
end

