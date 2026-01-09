--Dragão BAIANO
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	Duel.EnableGlobalFlag(GLOBALFLAG_SPSUMMON_COUNT)

	aux.AddFusionProcMix(
		c,
		true,
		true,
		s.matfilter1,
		s.matfilter2
	)

	-- If Fusion Summoned using 2 opponent's monsters (OBRIGATÓRIO)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOGRAVE)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(s.tgcon)
	e1:SetTarget(s.tgtg)
	e1:SetOperation(s.tgop)
	c:RegisterEffect(e1)

	-- Cannot attack
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_CANNOT_ATTACK)
	c:RegisterEffect(e2)

	-- Opponent Special Summon limit (2 per turn)
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_SPSUMMON_COUNT_LIMIT)
	e3:SetRange(LOCATION_MZONE)
	e3:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e3:SetTargetRange(0,1) -- apenas o oponente
	e3:SetValue(2)
	c:RegisterEffect(e3)
end

function s.matfilter1(c)
	return c:IsType(TYPE_MONSTER) and not c:IsRace(RACE_DRAGON)
end

function s.matfilter2(c)
	return c:IsType(TYPE_MONSTER) and not c:IsSetCard(0xfb3)
end

function s.tgcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsSummonType(SUMMON_TYPE_FUSION) then return false end
	local mg=c:GetMaterial()
	return mg and mg:GetCount()==2
		and mg:FilterCount(Card.IsControler,nil,1-tp)==2
end

function s.tgtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(Card.IsAbleToGrave,1-tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,nil,1,1-tp,LOCATION_DECK)
end

function s.tgop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_TOGRAVE)
	local g=Duel.SelectMatchingCard(1-tp,Card.IsAbleToGrave,1-tp,LOCATION_DECK,0,1,1,nil)
	if #g>0 then
		Duel.SendtoGrave(g,REASON_EFFECT)
	end
end
