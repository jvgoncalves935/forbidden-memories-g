--Miyuki Sone
local s,id=GetID()
function s.initial_effect(c)
	--position
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,1))
	e1:SetCategory(CATEGORY_POSITION)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetProperty(EFFECT_FLAG_CARD_TARGET+EFFECT_FLAG_DELAY)
	e1:SetCode(EVENT_SUMMON_SUCCESS)
	e1:SetCountLimit(1,id+200) -- hard once per turn
	e1:SetTarget(s.postg)
	e1:SetOperation(s.posop)
	c:RegisterEffect(e1)

	local e2=e1:Clone()
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e2)

	local e10=e1:Clone()
	e10:SetCode(EVENT_FLIP_SUMMON_SUCCESS)
	c:RegisterEffect(e10)

	--special summon (grave effect: banish 4 as cost, etc.)
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_GRAVE)
	e3:SetCost(s.spcost)
	e3:SetTarget(s.sptg)
	e3:SetOperation(s.spop)
	c:RegisterEffect(e3)

	--Becomes "Universo G" while on field, GY or banished
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_SINGLE)
	e4:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e4:SetCode(EFFECT_ADD_SETCODE)
	e4:SetRange(LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED)
	e4:SetValue(0xc50)
	c:RegisterEffect(e4)

	--Cannot Normal Summon/Set
	local e5=Effect.CreateEffect(c)
	e5:SetType(EFFECT_TYPE_SINGLE)
	e5:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e5:SetCode(EFFECT_CANNOT_SUMMON)
	c:RegisterEffect(e5)

	local e6=e5:Clone()
	e6:SetCode(EFFECT_CANNOT_MSET)
	c:RegisterEffect(e6)

	-- Change Level (5, 6 or 7) - soft once per turn
	local e7=Effect.CreateEffect(c)
	e7:SetDescription(aux.Stringid(id,1))
	e7:SetType(EFFECT_TYPE_IGNITION)
	e7:SetRange(LOCATION_MZONE)
	e7:SetCountLimit(1,id+400)
	e7:SetTarget(s.lvtg)
	e7:SetOperation(s.lvop)
	c:RegisterEffect(e7)

	-- Hand trigger: discard this card to draw 1 if a Fusion/Link/Ritual/Xyz/Synchro/Pendulum Summon occurs
	local e8=Effect.CreateEffect(c)
	e8:SetDescription(aux.Stringid(id,0))
	e8:SetCategory(CATEGORY_DRAW)
	e8:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e8:SetProperty(EFFECT_FLAG_DELAY)
	e8:SetCode(EVENT_SPSUMMON_SUCCESS)
	e8:SetRange(LOCATION_HAND)
	e8:SetCountLimit(1,id+600) -- hard once per turn
	e8:SetCondition(s.drcon)
	e8:SetCost(s.drcost)
	e8:SetTarget(s.drtg)
	e8:SetOperation(s.drop)
	c:RegisterEffect(e8)

	-- Register when this card is Special Summoned -> set player-flag so it cannot use grave effect again this turn
	local eReg=Effect.CreateEffect(c)
	eReg:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	eReg:SetCode(EVENT_SPSUMMON_SUCCESS)
	eReg:SetCondition(function(e,tp,eg,ep,ev,re,r,rp) return e:GetHandler():IsRelateToEffect(e) end)
	eReg:SetOperation(s.register_summon_flag)
	c:RegisterEffect(eReg)

	local e9=Effect.CreateEffect(c)
	e9:SetDescription(aux.Stringid(id,0))
	e9:SetType(EFFECT_TYPE_SINGLE)
	e9:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e9:SetCode(EFFECT_ADD_ATTRIBUTE)
	e9:SetRange(LOCATION_MZONE)
	e9:SetValue(ATTRIBUTE_LIGHT)
	c:RegisterEffect(e9)
end

function s.posfilter(c)
	return c:IsFaceup()
end

function s.postg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(1-tp) and s.posfilter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(s.posfilter,tp,0,LOCATION_MZONE,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local g=Duel.SelectTarget(tp,s.posfilter,tp,0,LOCATION_MZONE,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
end

function s.posop(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	if not tc or not tc:IsRelateToEffect(e) then return end

	-- tenta mudar a posição do alvo
	Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)

	-- se o alvo não ficou face-down DEF, obrigue o oponente a enviar esse card ao cemitério
	if not (tc:IsFacedown() and tc:IsDefensePos()) then
		-- só procede se o card ainda estiver no MZONE
		if not tc:IsLocation(LOCATION_MZONE) then return end
		-- pede para o oponente selecionar o card (só ele poderá escolher; filtro garante ser o mesmo card)
		Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_TOGRAVE)
		local g=Duel.SelectMatchingCard(1-tp,function(c) return c==tc end,1-tp,LOCATION_MZONE,0,1,1,nil)
		if g and #g>0 then
			-- envia para o cemitério sendo a ação do oponente (terceiro argumento = player who performs the send)
			Duel.SendtoGrave(g,REASON_RULE,1-tp)
		end
	end
end

function s.mainfilter(c)
	return c:IsLocation(LOCATION_MZONE) and c:GetSequence()<=4
end

-- NOTE: changed spcost to refuse activation if this card was already Summoned this turn
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	-- If card has been summoned this turn (player flag set), effect cannot be activated
	if Duel.GetFlagEffect(tp, id+400)~=0 then return false end

	local ft=Duel.GetLocationCount(tp,LOCATION_MZONE)
	local ct=-ft+1

	-- Grupo geral de cards que podem ser banidos
	local sg=Duel.GetMatchingGroup(Card.IsAbleToRemoveAsCost,tp,
		LOCATION_HAND+LOCATION_ONFIELD+LOCATION_GRAVE,0,e:GetHandler())

	-- Grupo que identifica cards do arquétipo Universo G (0xc50)
	local ug=sg:Filter(Card.IsSetCard,nil,0xc50)

	-- Pelo menos 1 deve ser Universo G
	if chk==0 then
		if sg:GetCount()<4 then return false end
		if ug:GetCount()==0 then return false end
		if ft<=0 and not sg:IsExists(s.mainfilter,ct,nil) then return false end
		return true
	end

	local g=Group.CreateGroup()

	-- Seleção quando o campo está cheio
	if ft<=0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
		-- Os que precisam sair da zona de monstros
		local g_req=sg:FilterSelect(tp,s.mainfilter,ct,ct,nil)
		g:Merge(g_req)

		-- removemos esses do grupo geral
		sg:Sub(g_req)

		-- Ainda precisamos selecionar (4 - ct)
		local remaining=4-ct

		-- Aqui aplicamos a regra: pelo menos 1 Universo G
		if not g:IsExists(Card.IsSetCard,1,nil,0xc50) then
			-- primeiro force 1 Universo G
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
			local ug_sel=sg:FilterSelect(tp,Card.IsSetCard,1,1,nil,0xc50)
			g:Merge(ug_sel)
			sg:Sub(ug_sel)
			remaining=remaining-1
		end

		if remaining>0 then
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
			local g2=sg:Select(tp,remaining,remaining,nil)
			g:Merge(g2)
		end

	else
		-- Campo com espaço
		-- Primeiro forçamos 1 Universo G
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
		local ug_sel=ug:Select(tp,1,1,nil)
		g:Merge(ug_sel)
		sg:Sub(ug_sel)

		-- Depois escolhemos os outros 3 livremente
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
		local g2=sg:Select(tp,3,3,nil)
		g:Merge(g2)
	end

	Duel.Remove(g,POS_FACEUP,REASON_COST)
end


function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false) and Duel.GetFlagEffect(tp,id+400)==0 end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:IsRelateToEffect(e) and Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)~=0 then
		-- After successful Special Summon, register the per-player flag to block further activations this turn
		if Duel.GetFlagEffect(tp,id+400)==0 then
			Duel.RegisterFlagEffect(tp,id+400,RESET_PHASE+PHASE_END,0,1)
		end
	end
end

-- registers flag when this card is Special Summoned by any effect (covers other summon sources)
function s.register_summon_flag(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local p=c:GetSummonPlayer()
	if Duel.GetFlagEffect(p,id+400)==0 then
		Duel.RegisterFlagEffect(p,id+400,RESET_PHASE+PHASE_END,0,1)
	end
end

-- Level change target & op
function s.lvtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(id,1))
	e:SetLabel(Duel.AnnounceNumber(tp,5,6,7))
end

function s.lvop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local lv=e:GetLabel()
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

function s.drcon(e,tp,eg,ep,ev,re,r,rp)
	return eg:IsExists(s.sumfilter,1,nil)
end

function s.sumfilter(c)
	-- precisa ser Invocação-Especial
	if c:GetSummonType()&SUMMON_TYPE_SPECIAL==0 then
		return false
	end

	-- precisa ser um dos tipos válidos
	return c:IsType(TYPE_FUSION)
		or c:IsType(TYPE_RITUAL)
		or c:IsType(TYPE_SYNCHRO)
		or c:IsType(TYPE_XYZ)
		or c:IsType(TYPE_LINK)
		or c:IsType(TYPE_PENDULUM)
end

function s.drcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsDiscardable() end
	Duel.SendtoGrave(c,REASON_COST+REASON_DISCARD)
end

function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.drop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Draw(tp,1,REASON_EFFECT)
end
