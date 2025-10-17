--Dragão Comunista do Imposto de Renda
local s,id,o=GetID()
function s.initial_effect(c)
	-- Regras de Invocação por Fusão
	c:EnableReviveLimit()
	aux.AddFusionProcFunRep(c,aux.TRUE,2,true) 
	-- ↑ aceita QUALQUER monstro como material (aux.TRUE)
	-- o “2” indica exatamente dois monstros
	-- o “true” significa que eles precisam ser diferentes no campo (não cópias)

	-- (Exemplo de efeito opcional ao ser invocado por Invocação-Fusão)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_DRAW)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCondition(s.drcon)
	e1:SetTarget(s.drtg)
	e1:SetOperation(s.drop)
	c:RegisterEffect(e1)
end

-- Condição: apenas se Invocado por Fusão
function s.drcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_FUSION)
end

-- Efeito exemplo: comprar 1 card
function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
	Duel.SetTargetPlayer(tp)
	Duel.SetTargetParam(1)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end
function s.drop(e,tp,eg,ep,ev,re,r,rp)
	local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
	Duel.Draw(p,d,REASON_EFFECT)
end
