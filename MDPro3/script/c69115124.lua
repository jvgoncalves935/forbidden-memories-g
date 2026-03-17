--Guardiões do Domínio das Trevas G
local s,id,o=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()

	-- Lista de materiais (opcional, mas útil para UI/compatibilidade)
	aux.AddMaterialCodeList(c,69115070,69115033,69115123)

	-- summon procedure
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_SINGLE)
	e0:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e0:SetCode(EFFECT_SPSUMMON_CONDITION)
	e0:SetValue(aux.fuslimit)
	c:RegisterEffect(e0)

	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_FUSION_MATERIAL)
	e1:SetCondition(s.fcondition)
	e1:SetOperation(s.foperation)
	c:RegisterEffect(e1)

	--negate
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_NEGATE+CATEGORY_DESTROY)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_CHAINING)
	e2:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DAMAGE_CAL)
	e2:SetRange(LOCATION_MZONE)
	e2:SetCondition(s.discon)
	e2:SetTarget(s.distg)
	e2:SetOperation(s.disop)
	c:RegisterEffect(e2)

	--destroyed
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_LEAVE_FIELD)
	e3:SetProperty(EFFECT_FLAG_DELAY)
	e3:SetCondition(s.spcon)
	e3:SetTarget(s.sptg)
	e3:SetOperation(s.spop)
	c:RegisterEffect(e3)
end

-- =========================
-- FUSION MATERIAL (SIMPLIFICADO)
-- =========================

function s.matfilter(c,fc)
	return c:IsCanBeFusionMaterial(fc)
		and (c:IsCode(69115007)
		or c:IsCode(69115033)
		or c:IsCode(69115123))
end

function s.fcondition(e,g,gc,chkf)
	if g==nil then return true end
	local c=e:GetHandler()
	local mg=g:Filter(s.matfilter,nil,c)

	return mg:IsExists(Card.IsCode,1,nil,69115007)
		and mg:IsExists(Card.IsCode,1,nil,69115033)
		and mg:IsExists(Card.IsCode,1,nil,69115123)
		and #mg>=3
end

function s.foperation(e,tp,eg,ep,ev,re,r,rp,gc,chkf)
	local c=e:GetHandler()
	local mg=eg:Filter(s.matfilter,nil,c)

	local g=Group.CreateGroup()

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
	g:AddCard(mg:FilterSelect(tp,Card.IsCode,1,1,nil,69115007):GetFirst())

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
	g:AddCard(mg:FilterSelect(tp,Card.IsCode,1,1,nil,69115033):GetFirst())

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
	g:AddCard(mg:FilterSelect(tp,Card.IsCode,1,1,nil,69115123):GetFirst())

	Duel.SetFusionMaterial(g)
end

-- =========================
-- RESTANTE DO SCRIPT (INALTERADO)
-- =========================

function s.discon(e,tp,eg,ep,ev,re,r,rp)
	return rp==1-tp and not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED) and Duel.IsChainNegatable(ev)
		and ((re:IsActiveType(TYPE_MONSTER) and Duel.GetFlagEffect(tp,id)==0)
		or (re:IsActiveType(TYPE_SPELL) and Duel.GetFlagEffect(tp,id+o)==0)
		or (re:IsActiveType(TYPE_TRAP) and Duel.GetFlagEffect(tp,id+o*2)==0))
end

function s.distg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_NEGATE,eg,1,0,0)

	if re:IsActiveType(TYPE_MONSTER) then
		Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
	elseif re:IsActiveType(TYPE_SPELL) then
		Duel.RegisterFlagEffect(tp,id+o,RESET_PHASE+PHASE_END,0,1)
	elseif re:IsActiveType(TYPE_TRAP) then
		Duel.RegisterFlagEffect(tp,id+o*2,RESET_PHASE+PHASE_END,0,1)
	end

	if re:GetHandler():IsDestructable() and re:GetHandler():IsRelateToEffect(re) then
		Duel.SetOperationInfo(0,CATEGORY_DESTROY,eg,1,0,0)
	end
end

function s.disop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.NegateActivation(ev) and re:GetHandler():IsRelateToEffect(re) then
		Duel.Destroy(eg,REASON_EFFECT)
	end
end

function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_ONFIELD)
		and c:IsPreviousPosition(POS_FACEUP)
		and c:IsPreviousControler(tp)
		and c:GetReasonPlayer()==1-tp
end

function s.spfilter(c,e,tp)
	return (c:IsSetCard(0xdd) or c:IsSetCard(0xcf) and c:IsAllTypes(TYPE_MONSTER+TYPE_RITUAL))
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and (c:IsLocation(LOCATION_GRAVE) and Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			or c:IsLocation(LOCATION_EXTRA) and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0)
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_GRAVE+LOCATION_EXTRA,0,1,nil,e,tp)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_GRAVE+LOCATION_EXTRA)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,aux.NecroValleyFilter(s.spfilter),tp,LOCATION_GRAVE+LOCATION_EXTRA,0,1,1,nil,e,tp)
	if #g>0 then
		Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)
	end
end