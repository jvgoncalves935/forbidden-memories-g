--Filhona
--c69115058
local s,id,o=GetID()
function s.initial_effect(c)
	-- Special Summon Procedure (sem chain)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id) -- HOPT principal
	e1:SetCondition(s.spcon)
	c:RegisterEffect(e1)

	-- Quick Effect no turno do oponente
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,0))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetRange(LOCATION_HAND)
	e2:SetCountLimit(1,id)
	e2:SetCondition(s.qcon)
	e2:SetTarget(s.qtg)
	e2:SetOperation(s.qop)
	c:RegisterEffect(e2)

	--Invocação-Fusão Rápida (igual ao efeito da Blazing Cartesia)
	local e3=Effect.CreateEffect(c)
	e3:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_MZONE)
	e3:SetHintTiming(0,TIMING_MAIN_END)
	e3:SetCountLimit(1,id+200)
	e3:SetCondition(s.condition)
	e3:SetTarget(s.target)
	e3:SetOperation(s.operation)
	c:RegisterEffect(e3)

	-- Special Summon "Ativo" ao ser Invocado
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,1))
	e4:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCode(EVENT_SUMMON_SUCCESS)
	e4:SetCountLimit(1,id+400)
	e4:SetTarget(s.atg)
	e4:SetOperation(s.aop)
	c:RegisterEffect(e4)

	local e5=e4:Clone()
	e5:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e5)

	local e6=e4:Clone()
	e6:SetCode(EVENT_FLIP_SUMMON_SUCCESS)
	c:RegisterEffect(e6)
end

-- Invocação-Especial se você controlar um monstro "Paulo Gino"
function s.spfilter(c)
	return c:IsFaceup() and c:IsSetCard(0xb39)
end

function s.spcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and (
			Duel.IsExistingMatchingCard(aux.TRUE,tp,0,LOCATION_ONFIELD,3,nil)
			or Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_MZONE,0,1,nil)
		)
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
	if c:IsRelateToEffect(e) then 
		Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
	end
end

function s.qcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetTurnPlayer()~=tp
		and (
			Duel.IsExistingMatchingCard(aux.TRUE,tp,0,LOCATION_ONFIELD,3,nil)
			or Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_MZONE,0,1,nil)
		)
end

function s.qtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
end

function s.qop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:IsRelateToEffect(e) then
		Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
	end
end

------------------------------------------------------------
-- Fusão Rápida (baseada em Blazing Cartesia)
------------------------------------------------------------
function s.condition(e,tp,eg,ep,ev,re,r,rp)
	local ph=Duel.GetCurrentPhase()
	return ph==PHASE_MAIN1 or ph==PHASE_MAIN2
end

function s.filter1(c,e)
	return not c:IsImmuneToEffect(e)
end

function s.filter2(c,e,tp,m,f,chkf)
	return c:IsType(TYPE_FUSION) and c:IsLevelAbove(8) and (not f or f(c))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)
		and c:CheckFusionMaterial(m,nil,chkf)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local mg=Duel.GetMatchingGroup(s.fusmatfilter,tp,
			LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,nil,e)
		return Duel.IsExistingMatchingCard(
			s.fusfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,mg
		)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
end


function s.operation(e,tp,eg,ep,ev,re,r,rp)
	local mg=Duel.GetMatchingGroup(
		s.fusmatfilter,tp,
		LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,nil,e
	)

	local sg=Duel.GetMatchingGroup(
		s.fusfilter,tp,LOCATION_EXTRA,0,nil,e,tp,mg
	)
	if #sg==0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local tc=sg:Select(tp,1,1,nil):GetFirst()
	if not tc then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
	local mat=Duel.SelectFusionMaterial(tp,tc,mg,nil,tp)

	tc:SetMaterial(mat)

	-- separar matérias por localização
	local g_grave=mat:Filter(Card.IsLocation,nil,LOCATION_GRAVE)
	local g_other=mat:Filter(function(c)
		return not c:IsLocation(LOCATION_GRAVE)
	end,nil)

	-- mão / campo → cemitério
	if #g_other>0 then
		Duel.SendtoGrave(
			g_other,
			REASON_EFFECT+REASON_MATERIAL+REASON_FUSION
		)
	end

	-- cemitério → deck
	if #g_grave>0 then
		Duel.SendtoDeck(
			g_grave,nil,SEQ_DECKSHUFFLE,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION
		)
	end

	Duel.BreakEffect()
	Duel.SpecialSummon(tc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)
	tc:CompleteProcedure()
end

function s.afilter(c,e,tp)
	return c:IsSetCard(0xe64)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and (
			c:IsLocation(LOCATION_HAND)
			or (c:IsLocation(LOCATION_EXTRA) and c:IsFaceup())
		)
end

function s.atg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingMatchingCard(
				s.afilter,tp,
				LOCATION_HAND+LOCATION_EXTRA,0,
				1,nil,e,tp
			)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND+LOCATION_EXTRA)
end

function s.aop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(
		tp,s.afilter,tp,
		LOCATION_HAND+LOCATION_EXTRA,0,
		1,1,nil,e,tp
	)
	local tc=g:GetFirst()
	if tc then
		Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
	end
end

function s.fusmatfilter(c,e)
	return c:IsCanBeFusionMaterial()
		and not c:IsImmuneToEffect(e)
		and (
			c:IsLocation(LOCATION_HAND)
			or c:IsLocation(LOCATION_MZONE)
			or c:IsLocation(LOCATION_GRAVE)
		)
end

function s.fusfilter(c,e,tp,mg)
	return c:IsType(TYPE_FUSION)
		and c:IsLevelAbove(8)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)
		and c:CheckFusionMaterial(mg,nil,tp)
end

