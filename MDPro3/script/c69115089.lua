--Ed Hector, O Maluco do Casebre
local s,id=GetID()
function s.initial_effect(c)
	-- Union
	aux.EnableUnionAttribute(c,s.unfilter)

	-- Union equip limit
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_SINGLE)
	e0:SetCode(EFFECT_UNION_LIMIT)
	e0:SetValue(s.eqlimit)
	c:RegisterEffect(e0)

	-- Special Summon rule (Kaiju-like) – opponent field
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetRange(LOCATION_HAND)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE+EFFECT_FLAG_SPSUM_PARAM)
	e1:SetTargetRange(POS_FACEUP_ATTACK,1)
	e1:SetCountLimit(1,id+200)
	e1:SetCondition(s.spcon1)
	e1:SetTarget(s.sptg1)
	e1:SetOperation(s.spop1)
	c:RegisterEffect(e1)

	-- Se ocorrer Invocação-Sincro enquanto equipado
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,2))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	e2:SetRange(LOCATION_SZONE)
	e2:SetCountLimit(1,id+400) -- hard OPT
	e2:SetCondition(s.spcon_eq)
	e2:SetTarget(s.sptg_eq)
	e2:SetOperation(s.spop_eq)
	c:RegisterEffect(e2)
end

function s.unfilter(c)
	return c:IsSetCard(0xc50) and c:IsAttackBelow(2000)
end

function s.eqlimit(e,c)
	return c:IsSetCard(0xc50) and c:IsAttackBelow(2000)
end

-- Kaiju-style Special Summon
function s.relfilter(c,tp)
	return c:IsReleasable(REASON_SPSUMMON)
		and Duel.GetMZoneCount(1-tp,c,tp)>0
end

function s.spcon1(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	return Duel.IsExistingMatchingCard(s.relfilter,tp,0,LOCATION_MZONE,1,nil,tp)
end

function s.sptg1(e,tp,eg,ep,ev,re,r,rp,chk,c)
	local g=Duel.GetMatchingGroup(s.relfilter,tp,0,LOCATION_MZONE,nil,tp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
	local tc=g:SelectUnselect(nil,tp,false,true,1,1)
	if tc then
		e:SetLabelObject(tc)
		return true
	end
	return false
end

function s.spop1(e,tp,eg,ep,ev,re,r,rp,c)
	local tc=e:GetLabelObject()
	if tc then
		Duel.Release(tc,REASON_SPSUMMON)
	end
end

-- Union → Special Summon on Synchro
function s.synfilter(c,tp)
	return c:IsSummonType(SUMMON_TYPE_SYNCHRO)
		and c:IsControler(tp)
end

function s.spcon_eq(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	-- verifica se está equipado
	if not c:GetEquipTarget() then return false end
	return eg:IsExists(s.synfilter,1,nil,tp)
end

function s.sptg_eq(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.spop_eq(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:GetEquipTarget() then return end
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)>0 then
		-- se quiser, aqui você pode forçar o unequip automaticamente
	end
end