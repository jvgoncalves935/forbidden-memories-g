--Vegeta de Família
--69115049
local s,id=GetID()
function s.initial_effect(c)
	--Habilita o efeito Pêndulo
	aux.EnablePendulumAttribute(c)
	
	--Efeito Pêndulo: destruir e invocar 1 Monstro Normal "Universo G" do Deck ou este card
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_DESTROY+CATEGORY_SPECIAL_SUMMON+CATEGORY_DRAW)
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_PZONE)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.spcon)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)
end

--------------------------------------------------------------
-- [Efeito Pêndulo]
--------------------------------------------------------------

-- Condição: requer outro card na Zona de Pêndulo
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetFieldGroupCount(tp,LOCATION_PZONE,0)>1
end

-- Filtro: Monstros Normais "Universo G" no Deck
function s.spfilter(c,e,tp)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_NORMAL)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-- Alvo: destrói este card e prepara a Invocação
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return c:IsDestructable() and Duel.GetLocationCount(tp,LOCATION_MZONE)>0
	end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,c,1,0,0)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_DECK+LOCATION_EXTRA)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
end

-- Operação: destrói, pergunta o tipo de Invocação, invoca e compra 2 cards
function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	Duel.SetChainLimitTillChainEnd(aux.FALSE)
	if not (c:IsRelateToEffect(e) and Duel.Destroy(c,REASON_EFFECT)~=0) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	
	-- Verifica se este card está no Extra Deck de face para cima
	local canSummonSelf=false
	if Duel.IsExistingMatchingCard(function(tc)
		return tc:IsFaceup() and tc:IsCode(id) and tc:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end,tp,LOCATION_EXTRA,0,1,nil) then
		canSummonSelf=true
	end

	local opt=0
	if canSummonSelf then
		opt=Duel.SelectOption(tp,aux.Stringid(id,2),aux.Stringid(id,3)) -- [0]=Deck / [1]=Este card
	else
		Duel.SelectOption(tp,aux.Stringid(id,2)) -- apenas opção Deck
	end

	-- 1ª opção: invocar Monstro Normal do Deck
	if opt==0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_DECK,0,1,1,nil,e,tp)
		if #g>0 then
			Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)
			Duel.BreakEffect()
			Duel.Draw(tp,2,REASON_EFFECT)
		end
	else
		-- 2ª opção: invocar o próprio card do Extra Deck
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local g=Duel.SelectMatchingCard(tp,function(tc)
			return tc:IsFaceup() and tc:IsCode(id) and tc:IsCanBeSpecialSummoned(e,0,tp,false,false)
		end,tp,LOCATION_EXTRA,0,1,1,nil)
		if #g>0 then
			Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)
			Duel.BreakEffect()
			Duel.Draw(tp,2,REASON_EFFECT)
		end
	end
end
