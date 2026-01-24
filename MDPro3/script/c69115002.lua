--Goleiro de Família
local s,id=GetID()
function s.initial_effect(c)

	-- Special Summon ao sofrer burn (hand / deck / grave)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_DAMAGE)
	e1:SetRange(LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCountLimit(1,id) -- hard once per turn
	e1:SetCondition(s.spcon)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- Não recebe dano por efeitos do oponente
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_CHANGE_DAMAGE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetTargetRange(1,0)
	e2:SetCondition(s.nodmgcon)
	e2:SetValue(s.damval)
	c:RegisterEffect(e2)

	-- Oponente não pode atacar diretamente
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_CANNOT_DIRECT_ATTACK)
	e3:SetRange(LOCATION_MZONE)
	e3:SetTargetRange(0,LOCATION_MZONE)
	c:RegisterEffect(e3)

end

function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	-- ep = quem recebeu o dano
	-- rp = quem causou
	-- r  = motivo
	return ep==tp
		and rp==1-tp
		and (r&REASON_EFFECT)~=0
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end

function s.nodmgcon(e)
	return e:GetHandler():IsFaceup()
end

function s.damval(e,re,val,r,rp,rc)
	-- Só zera dano causado pelo oponente e por efeito
	if rp==1-e:GetHandlerPlayer() and (r&REASON_EFFECT)~=0 then
		return 0
	end
	return val
end
