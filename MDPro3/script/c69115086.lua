-- Zeh Está Bolado - Bolado de Família
local s,id=GetID()
function s.initial_effect(c)
	-- Habilita Gemini (Dual)
	aux.EnableDualAttribute(c)

	-- Efeito Gemini
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND)
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCountLimit(1) -- soft once per turn
	e1:SetCondition(aux.IsDualState)
	e1:SetTarget(s.thtg)
	e1:SetOperation(s.thop)
	c:RegisterEffect(e1)

	-- Special Summon da mão revelando topo do Deck
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_REMOVE)
	e2:SetType(EFFECT_TYPE_IGNITION)
	e2:SetRange(LOCATION_HAND)
	e2:SetCountLimit(1,id+200) -- hard once per turn
	e2:SetTarget(s.sptg)
	e2:SetOperation(s.spop)
	c:RegisterEffect(e2)

end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SPELL+TYPE_TRAP)
		and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(
			s.thfilter,tp,
			LOCATION_DECK,0,1,nil
		)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,
		LOCATION_DECK)
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	-- 1) Adiciona Spell/Trap Universo G
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(
		tp,s.thfilter,tp,
		LOCATION_DECK,0,1,1,nil
	)
	if #g==0 then return end

	Duel.SendtoHand(g,nil,REASON_EFFECT)
	Duel.ConfirmCards(1-tp,g)

	-- 2) Envia este card ao Cemitério
	if c:IsRelateToEffect(e) then
		Duel.SendtoGrave(c,REASON_EFFECT)
	end

	-- 3) Extra Normal Summon (apenas 1 vez por turno)
	if Duel.GetFlagEffect(tp,id)==0 then
		Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)

		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_FIELD)
		e1:SetCode(EFFECT_EXTRA_SUMMON_COUNT)
		e1:SetTargetRange(LOCATION_HAND+LOCATION_MZONE,0)
		e1:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e1,tp)
	end

	-- 4) Lock de Invocação
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e2:SetTargetRange(1,0)
	e2:SetTarget(function(e,c)
		return not c:IsCode(id)
	end)
	e2:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e2,tp)

	local e3=e2:Clone()
	e3:SetCode(EFFECT_CANNOT_SUMMON)
	Duel.RegisterEffect(e3,tp)
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
			and Duel.GetDecktopGroup(tp,3):GetCount()==3
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
	Duel.SetOperationInfo(0,CATEGORY_REMOVE,nil,1,tp,LOCATION_DECK)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	if not c:IsRelateToEffect(e) then return end

	-- 1) Revela os 3 cards do topo do Deck
	local g=Duel.GetDecktopGroup(tp,3)
	if #g<3 then return end

	Duel.ConfirmCards(1-tp,g)

	-- 2) Oponente escolhe 1 para banir
	Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_REMOVE)
	local rg=g:Select(1-tp,1,1,nil)
	local rc=rg:GetFirst()
	if not rc then return end

	-- remove do grupo original
	g:RemoveCard(rc)

	-- banir
	Duel.Remove(rc,POS_FACEUP,REASON_EFFECT)

	-- 3) Special Summon deste card
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)==0 then
		return
	end

	-- 4) Retorna os restantes para o fundo do Deck (ordem escolhida pelo dono)
	if #g>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
		local sg=g:Select(tp,#g,#g,nil)
		Duel.SendtoDeck(sg,nil,SEQ_DECKBOTTOM,REASON_EFFECT)
	end
end

