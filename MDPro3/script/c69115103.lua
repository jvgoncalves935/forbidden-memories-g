--Nego Bam
--c69116103
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	-- 1 Universo G no campo + 4 monstros no campo
	aux.AddFusionProcFunFun(c, s.universe_g_filter, s.monster_on_field_filter, 4, true, true)

	-- Efeito: destruir cards se 3+ Universo G foram usados como matéria
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_DESTROY)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(s.descon)
	e1:SetTarget(s.destg)
	e1:SetOperation(s.desop)
	c:RegisterEffect(e1)

	-- Não pode ser tributado, usado como matéria ou destruído por efeitos
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_UNRELEASABLE_SUM)
	e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e2:SetValue(1)
	c:RegisterEffect(e2)
	local e3=e2:Clone()
	e3:SetCode(EFFECT_UNRELEASABLE_NONSUM)
	c:RegisterEffect(e3)
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_SINGLE)
	e4:SetProperty(EFFECT_FLAG_SINGLE_RANGE+EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
	e4:SetValue(1)
	c:RegisterEffect(e4)
end

function s.universe_g_filter(c)
	return c:IsSetCard(0xc50) and c:IsOnField() and c:IsType(TYPE_MONSTER)
end

-- Filtro: qualquer monstro no campo
function s.monster_on_field_filter(c)
	return c:IsOnField() and c:IsType(TYPE_MONSTER)
end

-- Filtro personalizado para garantir pelo menos 1 Universo G
function s.fusion_filter(c,fc,sub,mg,sg)
	if not c:IsSetCard(0xc50) then return false end
	-- Verifica se ainda precisamos garantir pelo menos 1 Universo G
	if sg and sg:IsExists(Card.IsSetCard,1,nil,0xc50) then
		return true -- já temos Universo G, qualquer monstro é válido
	end
	return c:IsSetCard(0xc50) -- ainda não usamos Universo G, este precisa ser
end

-- Condição: este card foi Invocado por Invocação-Fusão e usou 3+ Universo G
function s.descon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsSummonType(SUMMON_TYPE_FUSION) then return false end
	local mg=c:GetMaterial()
	return mg:FilterCount(Card.IsSetCard,nil,0xc50)>=3
end

-- Destroy all opponent's cards
function s.destg(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetFieldGroup(tp,0,LOCATION_ONFIELD)
	if chk==0 then return #g>0 end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,#g,0,0)
end
function s.desop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetFieldGroup(tp,0,LOCATION_ONFIELD)
	Duel.Destroy(g,REASON_EFFECT)
end
