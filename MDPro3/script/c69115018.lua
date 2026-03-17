--Yeah Man
local s,id=GetID()

function s.initial_effect(c)

	aux.EnablePendulumAttribute(c)

	-- Quick summon from hand
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e1:SetCountLimit(1,id)
	e1:SetCost(s.spcost)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_TO_GRAVE)
	e2:SetCountLimit(1,id+200)
	e2:SetTarget(s.pztg)
	e2:SetOperation(s.pzop)
	c:RegisterEffect(e2)

	local e3=e2:Clone()
	e3:SetCode(EVENT_REMOVE)
	e3:SetCondition(s.rmcon)
	c:RegisterEffect(e3)

	-- Used as material
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,2))
	e5:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e5:SetProperty(EFFECT_FLAG_DELAY)
	e5:SetCode(EVENT_BE_MATERIAL)
	e5:SetCountLimit(1,id+400)
	e5:SetCondition(s.matcon)
	e5:SetTarget(s.mattg)
	e5:SetOperation(s.matop)
	c:RegisterEffect(e5)

	-- Pendulum ATK boost
	local e6=Effect.CreateEffect(c)
	e6:SetType(EFFECT_TYPE_FIELD)
	e6:SetCode(EFFECT_UPDATE_ATTACK)
	e6:SetRange(LOCATION_PZONE)
	e6:SetTargetRange(LOCATION_MZONE,0)
	e6:SetTarget(s.atktg)
	e6:SetValue(400)
	c:RegisterEffect(e6)

	local e7=e6:Clone()
	e7:SetCode(EFFECT_UPDATE_DEFENSE)
	c:RegisterEffect(e7)

	-- Special from PZone
	local e8=Effect.CreateEffect(c)
	e8:SetDescription(aux.Stringid(id,3))
	e8:SetType(EFFECT_TYPE_QUICK_O)
	e8:SetCode(EVENT_FREE_CHAIN)
	e8:SetRange(LOCATION_PZONE)
	e8:SetCountLimit(1,id+600)
	e8:SetTarget(s.pstg)
	e8:SetOperation(s.psop)
	c:RegisterEffect(e8)

end

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsDiscardable() end
	
	Duel.SelectOption(tp,aux.Stringid(id,3),aux.Stringid(id,3))
	Duel.Hint(HINT_MESSAGE,tp,aux.Stringid(id,3))
	
	Duel.SendtoGrave(e:GetHandler(),REASON_COST+REASON_DISCARD)
end


-- materiais de fusão (diferença para Ursos Mansos: não inclui GY)
function s.fusmatfilter(c,e)
	return c:IsCanBeFusionMaterial()
		and not c:IsImmuneToEffect(e)
		and (
			c:IsLocation(LOCATION_HAND)
			or c:IsLocation(LOCATION_MZONE)
		)
end


-- verifica se um monstro do Extra pode ser invocado
function s.exfilter(c,e,tp)

	if not c:IsSetCard(0xc50) then return false end

	if c:IsType(TYPE_FUSION) then
		local mg=Duel.GetMatchingGroup(s.fusmatfilter,tp,LOCATION_HAND+LOCATION_MZONE,0,nil,e)
		return c:CheckFusionMaterial(mg,nil,tp)

	elseif c:IsType(TYPE_SYNCHRO) then
		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		return c:IsSynchroSummonable(nil,mg)

	elseif c:IsType(TYPE_XYZ) then
		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		return c:IsXyzSummonable(nil,mg)

	elseif c:IsType(TYPE_LINK) then
		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		return c:IsLinkSummonable(mg)

	end

	return false
end


function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)

	if chk==0 then
		return Duel.IsExistingMatchingCard(s.exfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp)
	end

	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)

end


function s.exgselect(g,exc,mc)
	return exc:IsXyzSummonable(g,#g,#g)
end


function s.spop(e,tp,eg,ep,ev,re,r,rp)

	local exg=Duel.GetMatchingGroup(s.exfilter,tp,LOCATION_EXTRA,0,nil,e,tp)
	if #exg==0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=exg:Select(tp,1,1,nil):GetFirst()
	if not sc then return end

	local mat=nil

	-- FUSION
	if sc:IsType(TYPE_FUSION) then

		local mg=Duel.GetMatchingGroup(s.fusmatfilter,tp,LOCATION_HAND+LOCATION_MZONE,0,nil,e)
		mat=Duel.SelectFusionMaterial(tp,sc,mg,nil,tp)

		sc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_FUSION)

		Duel.SpecialSummon(sc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)


	-- SYNCHRO
	elseif sc:IsType(TYPE_SYNCHRO) then

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SMATERIAL)
		mat=mg:SelectSubGroup(tp,function(g)
			return sc:IsSynchroSummonable(nil,g,#g-1,#g-1)
		end,false,2,#mg,tp,sc)

		if not mat then return end

		sc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_SYNCHRO)

		Duel.SpecialSummon(sc,SUMMON_TYPE_SYNCHRO,tp,tp,false,false,POS_FACEUP)


	-- XYZ
	elseif sc:IsType(TYPE_XYZ) then

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
		mat=mg:SelectSubGroup(tp,s.exgselect,false,1,#mg,sc,e:GetHandler())

		sc:SetMaterial(mat)
		Duel.Overlay(sc,mat)

		Duel.SpecialSummon(sc,SUMMON_TYPE_XYZ,tp,tp,false,false,POS_FACEUP)


	-- LINK
	elseif sc:IsType(TYPE_LINK) then

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_LMATERIAL)
		mat=mg:SelectSubGroup(tp,function(g)
			return sc:IsLinkSummonable(g)
		end,false,1,sc:GetLink())

		if not mat then return end

		sc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_LINK)

		Duel.SpecialSummon(sc,SUMMON_TYPE_LINK,tp,tp,false,false,POS_FACEUP)

	end

	sc:CompleteProcedure()

	Duel.SelectOption(tp,aux.Stringid(id,3),aux.Stringid(id,3))
	Duel.Hint(HINT_MESSAGE,tp,aux.Stringid(id,3))

end

function s.pztg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetFieldCard(tp,LOCATION_PZONE,0)==nil
			or Duel.GetFieldCard(tp,LOCATION_PZONE,1)==nil
	end
end

function s.pzop(e,tp)
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
			if Duel.SelectYesNo(tp,aux.Stringid(id,4)) then
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

function s.pendfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_PENDULUM)
		and not c:IsForbidden()
end

function s.matcon(e,tp,eg,ep,ev,re,r,rp)
	local r=e:GetHandler():GetReason()
	return (r&REASON_SYNCHRO~=0)
		or (r&REASON_FUSION~=0)
		or (r&REASON_LINK~=0)
end

function s.mattg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.matop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.IsExistingMatchingCard(s.pendfilter,tp,LOCATION_DECK,0,1,nil) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOEXTRA)
		local g=Duel.SelectMatchingCard(tp,s.pendfilter,tp,LOCATION_DECK,0,1,1,nil)
		if #g>0 then
			Duel.SendtoExtraP(g,tp,REASON_EFFECT)
		end
	end
end

function s.atktg(e,c)
	return c:IsSetCard(0xc50)
end

function s.pstg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
end

function s.psop(e,tp)
	local c=e:GetHandler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end

function s.rmcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsFaceup()
end