--Dragão Comunista do Imposto de Renda
--c69115109
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	-- Fusion Summon: 1 Universo G + 1 monstro no campo (pode ser do oponente)
	aux.AddFusionProcFun2(c,aux.FilterBoolFunction(Card.IsSetCard,0xc50),aux.FilterBoolFunction(Card.IsType,TYPE_MONSTER),true)

	-- Passivo: imposto de 600 LP quando o oponente ativa efeito de card
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e1:SetCode(EVENT_CHAINING)
	e1:SetRange(LOCATION_MZONE)
	e1:SetOperation(s.imposto)
	c:RegisterEffect(e1)

	-- Tributar Magia/Armadilha do oponente após invocação-fusão (escolha manual, face-up ou face-down)
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCondition(s.trcon)
	e2:SetTarget(s.trtg)
	e2:SetOperation(s.trop)
	c:RegisterEffect(e2)

	-- Special Summon do GY no início da Battle Phase
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,0))
	e3:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e3:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e3:SetCode(EVENT_PHASE+PHASE_BATTLE_START)
	e3:SetRange(LOCATION_GRAVE)
	e3:SetCountLimit(1,id)
	e3:SetTarget(s.sptg)
	e3:SetOperation(s.spop)
	c:RegisterEffect(e3)
end

-- Efeito passivo de imposto (sempre que o oponente ativa um efeito de card)
function s.imposto(e,tp,eg,ep,ev,re,r,rp)
	if rp~=tp then
		-- causa 600 de dano direto, mesmo que LP do oponente < 600
		Duel.Hint(HINT_CARD,0,id)
		Duel.Damage(1-tp,600,REASON_EFFECT)
	end
end

-- Filtro para Magia/Armadilha do oponente (face-up ou face-down)
function s.trfilter(c)
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsReleasableByEffect()
end

-- Condição: invocado por Fusão e usou matéria do oponente
function s.trcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsSummonType(SUMMON_TYPE_FUSION) and c:GetMaterial():IsExists(Card.IsControler,1,nil,1-tp)
end

-- Alvo: escolher Magia/Armadilha do oponente (face-up ou face-down)
function s.trtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(s.trfilter,tp,0,LOCATION_ONFIELD,nil)
	if chk==0 then return #g>0 end
	Duel.SetOperationInfo(0,CATEGORY_RELEASE,g,1,0,0)
end

-- Operação: tributar o card escolhido
function s.trop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(s.trfilter,tp,0,LOCATION_ONFIELD,nil)
	if #g>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
		local sg=g:Select(tp,1,1,nil)
		Duel.Release(sg,REASON_EFFECT+REASON_RULE)
	end
end

-- Filtro de Special Summon do GY
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_SPECIAL,tp,false,false) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

-- Special Summon do GY e dar 1300 LP para o oponente
function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:IsRelateToEffect(e) then
		Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
		Duel.Recover(1-tp,1300,REASON_EFFECT)
	end
end
