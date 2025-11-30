--Cabação
local s,id=GetID()

function s.initial_effect(c)
	-- Special Summon da mão sem ativar efeito
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_HAND)
	e1:SetCondition(s.spcon)
	c:RegisterEffect(e1)

		-----------------------------------------------------
	-- Trigger: SP "Filhona" ao ser Invocado OU enviado do Deck ao GY
	-----------------------------------------------------
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,0))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetCode(EVENT_SUMMON_SUCCESS)
	e2:SetProperty(EFFECT_FLAG_DELAY+EFFECT_FLAG_DAMAGE_STEP)
	e2:SetCountLimit(1,id) -- once per turn
	e2:SetTarget(s.sptg)
	e2:SetOperation(s.spop)
	c:RegisterEffect(e2)
	
	local e3=e2:Clone()
	e3:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e3)

	-- Enviado do Deck para o Cemitério
	local e4=e2:Clone()
	e4:SetCode(EVENT_TO_GRAVE)
	e4:SetCondition(s.gycon)
	c:RegisterEffect(e4)

end

-- condição: controlar Ativa ou Passiva ou Pendulum Universo G
function s.spcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()

	-- controla monstro "Ativa" ou "Passiva" no campo?
	local passivo = Duel.IsExistingMatchingCard(
		function(tc) return tc:IsFaceup() and (tc:IsSetCard(0x93b) or tc:IsSetCard(0x671)) end,
		tp,
		LOCATION_MZONE, 0, 1, nil
	)

	-- controla Pêndulo Universo G em Zona de Pêndulo?
	local pend_universog = Duel.IsExistingMatchingCard(
		function(tc)
			return tc:IsSetCard(0xc50) and tc:IsType(TYPE_PENDULUM)
		end,
		tp,
		LOCATION_PZONE, 0, 1, nil
	)

	return passivo or pend_universog
end

-- Verifica alvo SP
function s.spfilter(c,e,tp)
	return c:IsCode(69115058) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-- Target
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,nil,e,tp)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED)
end

-- Operation
function s.spop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_HAND+LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,1,nil,e,tp)
	local tc=g:GetFirst()
	if tc then
		Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
	end
end

-- Condição: foi enviado do Deck para o Cemitério
function s.gycon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_DECK)
end
