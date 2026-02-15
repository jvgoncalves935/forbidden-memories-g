--James Matarazzo
local s,id=GetID()
function s.initial_effect(c)
	--Habilita Pendulum Summon
	aux.EnablePendulumAttribute(c)

	-- SPECIAL SUMMON PROCEDURE (não gera chain)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,7))
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id,EFFECT_COUNT_CODE_OATH) -- hard OPT
	e1:SetCondition(s.spcon_proc)
	e1:SetTarget(s.sptg_proc)
	c:RegisterEffect(e1)

	-- QUICK EFFECT: Special summon quando o oponente ativa um card/efeito (EVENT_CHAINING)
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,7))
	e4:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e4:SetType(EFFECT_TYPE_QUICK_O)
	e4:SetCode(EVENT_CHAINING)
	e4:SetRange(LOCATION_HAND)
	e4:SetCountLimit(1,id,EFFECT_COUNT_CODE_OATH) -- mesmo hard OPT
	e4:SetCondition(s.spcon_chain)
	e4:SetTarget(s.sptg_quick)
	e4:SetOperation(s.spop_quick)
	c:RegisterEffect(e4)

	-- Quando for enviado ao GY
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,3))
	e5:SetCategory(CATEGORY_DESTROY)
	e5:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e5:SetProperty(EFFECT_FLAG_DELAY)
	e5:SetCode(EVENT_TO_GRAVE)
	e5:SetCountLimit(1,id+200,EFFECT_COUNT_CODE_OATH)
	e5:SetCondition(s.pendcon_gy)
	e5:SetTarget(s.pendtg)
	e5:SetOperation(s.pendop)
	c:RegisterEffect(e5)

	-- Quando for enviado ao Deck (Extra Deck)
	local e6=e5:Clone()
	e6:SetCode(EVENT_TO_DECK)
	e6:SetCondition(s.pendcon_extra)
	c:RegisterEffect(e6)

	-- OMNI-NEGATE
	local e7=Effect.CreateEffect(c)
	e7:SetDescription(aux.Stringid(id,4))
	e7:SetCategory(CATEGORY_NEGATE+CATEGORY_DESTROY+CATEGORY_SPECIAL_SUMMON)
	e7:SetType(EFFECT_TYPE_QUICK_O)
	e7:SetCode(EVENT_CHAINING)
	e7:SetRange(LOCATION_MZONE)
	e7:SetCountLimit(1,id+400) -- hard OPT próprio
	e7:SetCondition(s.negcon)
	e7:SetCost(s.negcost)
	e7:SetTarget(s.negtg)
	e7:SetOperation(s.negop)
	c:RegisterEffect(e7)

	-- PENDULUM EFFECT: Special Summon + Token opcional
	local e8=Effect.CreateEffect(c)
	e8:SetDescription(aux.Stringid(id,4))
	e8:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_TOKEN)
	e8:SetType(EFFECT_TYPE_QUICK_O)
	e8:SetCode(EVENT_FREE_CHAIN)
	e8:SetRange(LOCATION_PZONE)
	e8:SetCountLimit(1,id+600) -- hard OPT exclusivo deste efeito
	e8:SetTarget(s.pentg2)
	e8:SetOperation(s.penop2)
	c:RegisterEffect(e8)



end

-- Procedure: permite invocation no próprio turno OU no turno do oponente
-- usada pelo EFFECT_SPSUMMON_PROC
function s.spcon_proc(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
	-- pode no seu turno ou no turno do oponente (procedure aceita ambos)
	return true
end

function s.sptg_proc(e,tp,eg,ep,ev,re,r,rp,chk,c)
	return true
end

-- Quick-condition: apenas no turno do oponente
function s.spcon_quick(e,tp,eg,ep,ev,re,r,rp)
	-- só ativa como quick no turno do oponente
	if Duel.GetTurnPlayer()==tp then return false end
	-- precisa ter espaço e ser invocável
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
	local c=e:GetHandler()
	return c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-- Condição: o oponente ativou card/efeito
function s.spcon_chain(e,tp,eg,ep,ev,re,r,rp)
	-- O oponente ativou algo
	if rp==tp then return false end

	-- espaço no campo
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end

	-- pode ser invocado?
	local c=e:GetHandler()
	return c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-- Quick target/operação (executa SpecialSummon)
function s.sptg_quick(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.spop_quick(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	-- realiza Special Summon (como efeito/Quick)
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)~=0 then
		-- opcional: registrar flag se quiser impedir outra forma de summon no mesmo turno
		-- (mas o CountLimit compartilhado já evita que seja usado duas vezes)
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
		c:IsPreviousLocation(LOCATION_REMOVED)) or 
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
		c:IsPreviousLocation(LOCATION_REMOVED)) or 
		c:IsPreviousLocation(LOCATION_OVERLAY))
end

function s.negcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	-- card precisa estar na MZone do dono original
	if c:GetControler()~=tp then return false end
	if not c:IsLocation(LOCATION_MZONE) then return false end

	-- não pode negar Summons, apenas efeitos
	if not re:IsActivated() then return false end

	-- o efeito é negável?
	return Duel.IsChainNegatable(ev)
end

function s.negcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end

	local c=e:GetHandler()

	-- opções disponíveis ao jogador
	local op=0
	local canNegDestroy = Duel.IsExistingMatchingCard(
		function(tc) return tc:IsFaceup() and tc:IsSetCard(0xc50) and tc:IsLevelBelow(4) end,
		tp, LOCATION_MZONE, LOCATION_MZONE, 1, nil
	)

	local canSS = Duel.IsExistingMatchingCard(
		function(tc) return tc:IsSetCard(0xe64) or tc:IsSetCard(0x93b) end,
		tp, LOCATION_DECK, 0, 1, nil, e, tp
	)

	local options = {}
	if canNegDestroy then table.insert(options, aux.Stringid(id,4)) end
	if canSS then table.insert(options, aux.Stringid(id,5)) end

	-- força escolha se ambas opções existirem
	if #options==2 then
		op=Duel.SelectOption(tp, aux.Stringid(id,4), aux.Stringid(id,5))
	elseif canNegDestroy then
		op=0
	else
		op=1
	end

	-- guarda escolha:
	-- 0 = negar + destruir Universo G
	-- 1 = Special Summon Ativo/Ativa
	e:SetLabel(op+1)
end

function s.negtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end

	local op=e:GetLabel()

	if op==1 then
		-- negar + destruir Universo G
		Duel.SetOperationInfo(0, CATEGORY_NEGATE, eg, 1, 0, 0)
		Duel.SetOperationInfo(0, CATEGORY_DESTROY, nil, 1, tp, LOCATION_MZONE)
	else
		-- enviar 1 card do Deck para o Cemitério
		Duel.SetOperationInfo(0, CATEGORY_TOGRAVE, nil, 1, tp, LOCATION_DECK)
	end
end

function s.negop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	local op=e:GetLabel()

	-- 1 → negar + destruir Universo G
	if op==1 then
		if Duel.NegateActivation(ev) then
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
			local g=Duel.SelectMatchingCard(tp,
				function(tc) return tc:IsFaceup() and tc:IsSetCard(0xc50) and tc:IsLevelBelow(4) end,
				tp, LOCATION_MZONE, LOCATION_MZONE, 1, 1, nil
			)
			if #g>0 then
				Duel.Destroy(g, REASON_EFFECT)
			end
		end

	-- 2 → enviar 1 card do Deck para o Cemitério
	else
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
		local g=Duel.SelectMatchingCard(tp,
			function(tc) return tc:IsAbleToGrave() end,
			tp, LOCATION_DECK, 0, 1, 1, nil
		)
		if #g>0 then
			Duel.SendtoGrave(g, REASON_EFFECT)
		end
	end
end

-- Target: apenas verifica se dá pra invocar este card da P-Zone
function s.pentg2(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

-- Operation completa
function s.penop2(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end

	-- 1) Invocar o próprio card da P-Zone
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)==0 then return end

	-- 2) Após invocar, verificar SE é o único monstro do jogador
	if Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)>1 then return end

	-- 3) Perguntar se o jogador quer criar a ficha
	if not Duel.SelectYesNo(tp,aux.Stringid(id,6)) then return end

	-- 4) Jogador escolhe nível 3~6
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_LVRANK)
	local lv=Duel.AnnounceLevel(tp,3,6)
	if not lv then return end

	-- Verificar espaço de novo
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end

	-- 5) Criar a Ficha
	local token=Duel.CreateToken(tp, 69069005)
	if not token then return end
	
	-- Invoca a ficha
	Duel.SpecialSummon(token,0,tp,tp,false,false,POS_FACEUP)

	-- Aplica Level escolhido
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_CHANGE_LEVEL)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
	e1:SetValue(lv)
	e1:SetReset(RESET_EVENT+RESETS_STANDARD)
	token:RegisterEffect(e1,true)

	-- Define Setcode "Universo G"
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_ADD_SETCODE)
	e2:SetValue(0xc50)
	e2:SetReset(RESET_EVENT+RESETS_STANDARD)
	token:RegisterEffect(e2,true)

	-- necessário para alguns tokens reconhecerem efeitos contínuos
	token:SetStatus(STATUS_PROC_COMPLETE,true)

end

