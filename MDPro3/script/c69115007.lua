--Jailson Mendes, O Pai de Família
local s,id,o=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	aux.EnablePendulumAttribute(c)
	
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_FIELD)
	e0:SetCode(EFFECT_SPSUMMON_PROC)
	e0:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e0:SetRange(LOCATION_EXTRA)
	e0:SetCondition(s.xyzcon)
	e0:SetOperation(s.xyzop)
	e0:SetValue(SUMMON_TYPE_XYZ)
	c:RegisterEffect(e0)
	
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCountLimit(1,id+200)
	e1:SetCondition(s.thcon)
	e1:SetCost(s.thcost)
	e1:SetTarget(s.thtg)
	e1:SetOperation(s.thop)
	c:RegisterEffect(e1)

	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e2:SetCode(EVENT_CHAIN_SOLVING)
	e2:SetRange(LOCATION_PZONE)
	e2:SetCountLimit(1)
	e2:SetCondition(s.pendcon)
	e2:SetOperation(s.pendop)
	c:RegisterEffect(e2)

	-- Move to Pendulum Zone if used as material
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e3:SetProperty(EFFECT_FLAG_DELAY)
	e3:SetCode(EVENT_BE_MATERIAL)
	e3:SetCountLimit(1,id+400) -- hard once per turn separado
	e3:SetCondition(s.matcond)
	e3:SetTarget(s.pentg)
	e3:SetOperation(s.penop)
	c:RegisterEffect(e3)

	-- Block additional Xyz summons of this card while player flag is set (prevents >1 per turn)
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_SINGLE)
	e4:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e4:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e4:SetCondition(s.block_if_flag)
	e4:SetValue(s.xyzlimit)
	c:RegisterEffect(e4)

	-- Can attack while in Defense Position
	local e5=Effect.CreateEffect(c)
	e5:SetType(EFFECT_TYPE_SINGLE)
	e5:SetCode(EFFECT_DEFENSE_ATTACK)
	e5:SetValue(1)
	c:RegisterEffect(e5)
end

function s.xyzcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	local g=Duel.GetMatchingGroup(s.xyzfilter,tp,LOCATION_MZONE+LOCATION_PZONE,0,nil)
	return g:CheckSubGroup(s.xyzcheck,2,2)
end

function s.xyzop(e,tp,eg,ep,ev,re,r,rp,c)
	local g=Duel.GetMatchingGroup(s.xyzfilter,tp,LOCATION_MZONE+LOCATION_PZONE,0,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local sg=g:SelectSubGroup(tp,s.xyzcheck,false,2,2)
	c:SetMaterial(sg)
	Duel.Overlay(c,sg)

	Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
end

function s.xyz_type(c)
	if c:IsType(TYPE_FUSION) then return TYPE_FUSION end
	if c:IsType(TYPE_SYNCHRO) then return TYPE_SYNCHRO end
	if c:IsType(TYPE_XYZ) then return TYPE_XYZ end
	if c:IsType(TYPE_LINK) then return TYPE_LINK end
	if c:IsType(TYPE_RITUAL) then return TYPE_RITUAL end
	return 0
end

function s.xyzfilter(c)
	if not (c:IsFaceup() and c:IsSetCard(0xc50)) then return false end

	local t = s.xyz_type(c)
	if t==0 then return false end

	-- Checagem de Level / Rank / Link
	if t==TYPE_FUSION or t==TYPE_SYNCHRO or t==TYPE_RITUAL then
		if c:GetLevel()<6 then return false end
	elseif t==TYPE_XYZ then
		if c:GetRank()<6 then return false end
	elseif t==TYPE_LINK then
		if c:GetLink()<2 then return false end
	end

	-- Se estiver na Zona de Pêndulo, precisa poder virar Matéria-Xyz
	if c:IsLocation(LOCATION_PZONE) then
		return c:IsCanBeXyzMaterial()
	end

	return c:IsType(TYPE_MONSTER)
end

function s.xyzcheck(g)
	if #g~=2 then return false end
	local t1=s.xyz_type(g:GetFirst())
	local t2=s.xyz_type(g:GetNext())
	return t1~=t2
end

function s.thfilter(c)
	return c:IsCode(69115061,69115096,69069008,69115058,69115116)
		and c:IsAbleToHand()
end

function s.thcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_XYZ)
end

function s.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	local ct=c:GetOverlayCount()
	if chk==0 then
		return ct>0
	end
	c:RemoveOverlayCard(tp,ct,ct,REASON_COST)
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(
			s.thfilter,tp,
			LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,nil
		)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,
		LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED)
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,
		LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,tp,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
end

function s.negfilter(re,tp)
	if not re:IsActivated() then return false end
	if re:GetOwnerPlayer()==tp then return false end

	local cat=re:GetCategory()

	-- Sempre permitir destruir ou banir
	if (cat&(CATEGORY_DESTROY|CATEGORY_REMOVE))~=0 then
		return true
	end

	-- Para TOHAND / TODECK: apenas se afetar cartas no campo
	if (cat&(CATEGORY_TOHAND|CATEGORY_TODECK))~=0 then
		local exg=Duel.GetOperationInfo(0,CATEGORY_TOHAND)
		if not exg then
			exg=Duel.GetOperationInfo(0,CATEGORY_TODECK)
		end
		if not exg then return false end

		local g=exg
		return g:IsExists(Card.IsOnField,1,nil)
	end

	return false
end

function s.pendcon(e,tp,eg,ep,ev,re,r,rp)
	return s.negfilter(re,tp)
end

function s.pendop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsDestructable() then return end
	if not Duel.SelectYesNo(tp,aux.Stringid(id,4)) then return end

	if Duel.Destroy(c,REASON_EFFECT)>0 then
		Duel.NegateEffect(ev)
	end
end

function s.matcond(e,tp,eg,ep,ev,re,r,rp)
	return r&(REASON_FUSION|REASON_SYNCHRO|REASON_LINK)~=0
end

function s.pentg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetFieldCard(tp,LOCATION_PZONE,0)==nil
			or Duel.GetFieldCard(tp,LOCATION_PZONE,1)==nil
	end
end

function s.penop(e,tp,eg,ep,ev,re,r,rp)
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

-- Block condition based on Duel flag (one Xyz Summon of this card per player per turn)
function s.block_if_flag(e)
	local tp=e:GetHandlerPlayer()
	return Duel.GetFlagEffect(tp,id)~=0
end

-- limit only for Xyz Summons
function s.xyzlimit(e,c,sump,sumtype,sumpos,targetp,se)
	return sumtype==SUMMON_TYPE_XYZ
end

