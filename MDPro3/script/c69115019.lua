--Mangueira Evil
local s,id=GetID()
function s.initial_effect(c)
	-- Special Summon Procedure (sem chain)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id) -- hard OPT compartilhado
	e1:SetCondition(s.spcon_proc)
	c:RegisterEffect(e1)

	-- Quick Effect: Special Summon from hand
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,0))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_CHAINING)
	e2:SetRange(LOCATION_HAND)
	e2:SetCountLimit(1,id)
	e2:SetCondition(s.qspcon)
	e2:SetTarget(s.qsptg)
	e2:SetOperation(s.qspop)
	c:RegisterEffect(e2)

	-- If this card is Summoned: You can change its Level to 2
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e3:SetProperty(EFFECT_FLAG_DELAY)
	e3:SetCode(EVENT_SUMMON_SUCCESS)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id+200) -- hard OPT
	e3:SetOperation(s.lvop)
	c:RegisterEffect(e3)

	local e4=e3:Clone()
	e4:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e4)

	local e5=e3:Clone()
	e5:SetCode(EVENT_FLIP_SUMMON_SUCCESS)
	c:RegisterEffect(e5)

	-- Quick Effect: Special Summon + Xyz Summon
	local e6=Effect.CreateEffect(c)
	e6:SetDescription(aux.Stringid(id,3))
	e6:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e6:SetType(EFFECT_TYPE_QUICK_O)
	e6:SetCode(EVENT_FREE_CHAIN)
	e6:SetRange(LOCATION_MZONE)
	e6:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE)
	e6:SetCountLimit(1,id+400) -- hard OPT
	e6:SetTarget(s.xyztg)
	e6:SetOperation(s.xyzop)
	c:RegisterEffect(e6)

end

function s.spcon_proc(e,c)
	if c==nil then return true end
	return Duel.GetLocationCount(c:GetControler(),LOCATION_MZONE)>0
end

function s.qspcon(e,tp,eg,ep,ev,re,r,rp)
	return rp==1-tp and re:IsActivated()
end

function s.qsptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.qspop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	if not c:IsRelateToEffect(e) then return end
	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end

function s.lvop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local lv=2
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		-- Set level to announced value (replace current level)
		local cur=c:GetLevel()
		if cur~=lv then
			local e1=Effect.CreateEffect(c)
			e1:SetType(EFFECT_TYPE_SINGLE)
			e1:SetCode(EFFECT_UPDATE_LEVEL)
			e1:SetValue(lv - cur)
			e1:SetReset(RESET_EVENT+RESETS_STANDARD)
			c:RegisterEffect(e1)
		end
	end
end

function s.deckfilter_tg(c,lv)
	return c:IsSetCard(0xc50)
		and c:IsLevel(lv)
end


function s.basefilter(c,tp)
	local lv=c:GetLevel()
	return c:IsFaceup()
		and c:IsSetCard(0xc50)
		and lv<=6
		and Duel.IsExistingMatchingCard(s.deckfilter_tg,tp,LOCATION_DECK,0,1,nil,lv)
		and Duel.IsExistingMatchingCard(s.xyzfilter,tp,LOCATION_EXTRA,0,1,nil,lv)
end

function s.deckfilter(c,lv,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsLevel(lv)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

function s.matfilter(c,lv)
	return c:IsFaceup()
		and c:IsSetCard(0xc50)
		and c:IsLevel(lv)
end

function s.xyzfilter(c,lv)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_XYZ)
		and c:GetRank()==lv
		and c:GetRank()<=6
end

function s.xyztg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
		return Duel.IsExistingMatchingCard(s.basefilter,tp,LOCATION_MZONE,0,1,nil,tp)
	end
end

function s.xyzop(e,tp,eg,ep,ev,re,r,rp)
	-- Seleciona o monstro base CORRETO
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local base=Duel.SelectMatchingCard(tp,s.basefilter,tp,LOCATION_MZONE,0,1,1,nil,tp):GetFirst()
	if not base then return end
	local lv=base:GetLevel()

	-- Invoca do Deck
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.deckfilter,tp,LOCATION_DECK,0,1,1,nil,lv,e,tp)
	local sc=g:GetFirst()
	if not sc then return end
	if Duel.SpecialSummon(sc,0,tp,tp,false,false,POS_FACEUP)==0 then return end

	-- Nega efeitos do monstro invocado
	local e1=Effect.CreateEffect(e:GetHandler())
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_DISABLE)
	e1:SetReset(RESET_EVENT+RESETS_STANDARD)
	sc:RegisterEffect(e1)

	local e2=e1:Clone()
	e2:SetCode(EFFECT_DISABLE_EFFECT)
	sc:RegisterEffect(e2)

	-- Grupo EXATO de matérias
	local mg=Group.CreateGroup()
	mg:AddCard(base)
	mg:AddCard(sc)

	-- Seleciona o Xyz válido
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local xyz=Duel.SelectMatchingCard(tp,s.xyzfilter,tp,LOCATION_EXTRA,0,1,1,nil,lv):GetFirst()
	if not xyz then return end

	-- Invocação-Xyz manual CORRETA
	xyz:SetMaterial(mg)
	Duel.Overlay(xyz,mg)

	if Duel.SpecialSummon(xyz,SUMMON_TYPE_XYZ,tp,tp,false,false,POS_FACEUP)>0 then
		xyz:CompleteProcedure()
	end

	-- Lock de Xyz
	local e3=Effect.CreateEffect(e:GetHandler())
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e3:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e3:SetTargetRange(1,0)
	e3:SetTarget(function(e,c)
		return c:IsType(TYPE_XYZ)
	end)
	e3:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e3,tp)
end
