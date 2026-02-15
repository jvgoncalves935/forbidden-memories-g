--Bizarro de Família
local s,id=GetID()

function s.initial_effect(c)
	aux.EnablePendulumAttribute(c)

	-- 1) Sempre é Não-Regulador no campo
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_SINGLE)
	e0:SetCode(EFFECT_NONTUNER)
	e0:SetRange(LOCATION_MZONE)
	e0:SetValue(1)
	c:RegisterEffect(e0)

	-- 3) Ritual da mão (Quick Effect)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_RELEASE)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id) -- hard OPT
	e1:SetTarget(s.rittg)
	e1:SetOperation(s.ritop)
	c:RegisterEffect(e1)

	-- 4) Busca Level 1 (Ignition)
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_TOHAND)
	e2:SetType(EFFECT_TYPE_IGNITION)
	e2:SetRange(LOCATION_MZONE)
	e2:SetCountLimit(1,id+200) -- hard OPT separado
	e2:SetTarget(s.thtg)
	e2:SetOperation(s.thop)
	c:RegisterEffect(e2)

	-- 5) Pendulum Effect (Quick, soft OPT)
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetCategory(CATEGORY_TOHAND)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_PZONE)
	e3:SetCountLimit(1) -- soft OPT
	e3:SetTarget(s.pentg)
	e3:SetOperation(s.penop)
	c:RegisterEffect(e3)

	-- Quando for enviado ao GY
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,3))
	e4:SetCategory(CATEGORY_DESTROY)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCode(EVENT_TO_GRAVE)
	e4:SetCountLimit(1,id+200,EFFECT_COUNT_CODE_OATH)
	e4:SetCondition(s.pendcon_gy)
	e4:SetTarget(s.pendtg)
	e4:SetOperation(s.pendop)
	c:RegisterEffect(e4)

	-- Quando for enviado ao Deck (Extra Deck)
	local e5=e4:Clone()
	e5:SetCode(EVENT_TO_DECK)
	e5:SetCondition(s.pendcon_extra)
	c:RegisterEffect(e5)
end

function s.ritfilter(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsLevelBelow(3)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

function s.rittg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingMatchingCard(s.ritfilter,tp,LOCATION_DECK,0,1,nil,e,tp)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_DECK)
	Duel.SetOperationInfo(0,CATEGORY_RELEASE,e:GetHandler(),1,0,0)
end

function s.ritop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	if not c:IsRelateToEffect(e) then return end

	-- 1) Special Summon do Deck
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.ritfilter,tp,LOCATION_DECK,0,1,1,nil,e,tp)
	local tc=g:GetFirst()
	if not tc then return end

	Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)

	-- Tributar da mão
	if Duel.Release(c,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)==0 then return end

	-- Ritual Summon do próprio card
	Duel.SpecialSummonStep(c,SUMMON_TYPE_RITUAL,tp,tp,true,false,POS_FACEUP)
	c:SetMaterial(Group.FromCards(c))
	Duel.SpecialSummonComplete()
	c:CompleteProcedure()
end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsLevel(1)
		and c:IsType(TYPE_MONSTER)
		and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
end

function s.penfilter(c)
	return c:IsSetCard(0xc50)
		and (
			(c:IsType(TYPE_RITUAL) and c:IsType(TYPE_MONSTER))
			or (c:IsLevel(1) and c:IsType(TYPE_MONSTER))
		)
		and c:IsAbleToHand()
end

function s.pentg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.penfilter,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.penop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.penfilter,tp,LOCATION_DECK,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
end

function s.pendcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	-- O card saiu do campo e agora está:
	-- 1) no Cemitério, ou
	-- 2) no Extra Deck face-up (padrão Pendulum)
	return (c:IsLocation(LOCATION_GRAVE))
		or (c:IsLocation(LOCATION_EXTRA) and c:IsFaceup())
end

-- Target: verifica disponibilidade e declara info de destruição
function s.pendtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		-- ativação permitida sempre que houver ao menos 1 espaço ou ambas ocupadas (porque pode ser obrigatório destruir)
		-- mas devolvemos true (a condição de ativação já está na trigger)
		return true
	end

	-- verifica o estado das PZones
	local left = Duel.GetFieldCard(tp,LOCATION_PZONE,0)
	local right = Duel.GetFieldCard(tp,LOCATION_PZONE,1)
	local both_full = left and right

	if both_full then
		-- obrigatoriamente destruir 1 (anuncia destruição)
		local g=Group.FromCards(left,right)
		Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
	else
		-- opcional: pode destruir até 1 (se existir)
		local g=Group.CreateGroup()
		if left then g:AddCard(left) end
		if right then g:AddCard(right) end
		if #g>0 then
			Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
		end
	end
end

-- Operation: destrói e depois MoveToField para PZone se houver espaço
function s.pendop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	local left = Duel.GetFieldCard(tp,LOCATION_PZONE,0)
	local right = Duel.GetFieldCard(tp,LOCATION_PZONE,1)
	local both_full = left and right

	-- 1) Destruição
	if both_full then
		-- há duas cartas: escolha obrigatória de qual destruir
		local g=Group.FromCards(left,right)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
		local sg=g:Select(tp,1,1,nil)
		if Duel.Destroy(sg,REASON_EFFECT)==0 then return end
	else
		-- se houver ao menos 1 carta nas PZones, perguntamos se o usuário quer destruir
		local g=Group.CreateGroup()
		if left then g:AddCard(left) end
		if right then g:AddCard(right) end
		if #g>0 then
			if Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
				Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
				local sg=g:Select(tp,1,1,nil)
				if Duel.Destroy(sg,REASON_EFFECT)==0 then return end
			end
		end
	end

	-- 2) Mover para PZone se houver espaço
	local canLeft = Duel.CheckLocation(tp,LOCATION_PZONE,0)
	local canRight = Duel.CheckLocation(tp,LOCATION_PZONE,1)

	if not (canLeft or canRight) then
		-- nenhuma PZone livre: nada a fazer
		return
	end

	-- se existir apenas uma livre, movemos para ela; se ambas livres, perguntamos ao jogador
	if canLeft and not canRight then
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		return
	elseif canRight and not canLeft then
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		return
	else
		-- ambas livres. A engine normalmente colocará em uma PZone livre.
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		return
	end
end

-- Se foi enviado ao GY de QUALQUER LUGAR
function s.pendcon_gy(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsLocation(LOCATION_GRAVE) and 
		(c:IsPreviousLocation(LOCATION_ONFIELD) or
		c:IsPreviousLocation(LOCATION_HAND) or
		c:IsPreviousLocation(LOCATION_DECK) or
		c:IsPreviousLocation(LOCATION_EXTRA) or
		c:IsPreviousLocation(LOCATION_REMOVED) or 
		c:IsPreviousLocation(LOCATION_OVERLAY))
end

-- Se foi enviado ao Extra Deck face-up (padrão pendulum)
function s.pendcon_extra(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsFaceup() and c:IsLocation(LOCATION_EXTRA) and
		(c:IsPreviousLocation(LOCATION_ONFIELD) or
		c:IsPreviousLocation(LOCATION_HAND) or
		c:IsPreviousLocation(LOCATION_DECK) or
		c:IsPreviousLocation(LOCATION_GRAVE) or
		c:IsPreviousLocation(LOCATION_REMOVED) or 
		c:IsPreviousLocation(LOCATION_OVERLAY))
end
