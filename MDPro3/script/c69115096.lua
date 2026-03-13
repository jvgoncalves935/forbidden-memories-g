--Ursos Grandes, Peludos e Mansos!
local s,id=GetID()

function s.initial_effect(c)
	-- Activate
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCountLimit(1,id)
	e1:SetCost(s.cost)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- Pode ativar da mão no turno do oponente sob condição especial
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_QP_ACT_IN_NTPHAND)
	e2:SetCondition(s.handcon)
	c:RegisterEffect(e2)
end


function s.cfilter(c)
	return c:IsReleasable()
end

function s.handcon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.GetTurnPlayer()~=tp
		and Duel.GetTurnCount()==1
		and Duel.GetFieldGroupCount(tp,LOCATION_SZONE,0)==0
end

-- Tribute 1 card you control
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_ONFIELD,0,1,e:GetHandler())
	end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
	local g=Duel.SelectMatchingCard(tp,s.cfilter,tp,LOCATION_ONFIELD,0,1,1,e:GetHandler())
	Duel.Release(g,REASON_COST)
end

-- reutiliza filtro do Yeah Man
function s.spfilter(c,e,tp)
	if not c:IsSetCard(0xc50) then return false end

	if c:IsType(TYPE_FUSION) then
		return Duel.IsExistingMatchingCard(s.fusmat,tp,
			LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,1,nil,c,tp)
	elseif c:IsType(TYPE_SYNCHRO) then
		return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,LOCATION_MZONE,0,1,nil)
	elseif c:IsType(TYPE_XYZ) then
		return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,LOCATION_MZONE,0,2,nil)
	elseif c:IsType(TYPE_LINK) then
		return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,LOCATION_MZONE,0,1,nil)
	end
	return false
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp)
	end
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)

	local mg_field=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

	-- diferença principal: inclui GY
	local mg_fusion=Duel.GetMatchingGroup(Card.IsType,tp,
		LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,nil,TYPE_MONSTER)

	local exg=Duel.GetMatchingGroup(s.exfilter,tp,LOCATION_EXTRA,0,nil,mg_field,mg_fusion)
	if #exg==0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=exg:Select(tp,1,1,nil):GetFirst()
	if not sc then return end

	local mg=sc:IsType(TYPE_FUSION) and mg_fusion or mg_field

	local mat=s.selectmaterials(tp,mg,sc)
	if not mat then return end

	s.specialfromextra(tp,sc,mat)

end

-- mesmas funções do Yeah Man
function s.materialcheck(sc,g)
	if sc:IsType(TYPE_FUSION) then
		return sc:CheckFusionMaterial(g,nil,sc:GetControler())
	elseif sc:IsType(TYPE_SYNCHRO) then
		return sc:IsSynchroSummonable(nil,g)
	elseif sc:IsType(TYPE_XYZ) then
		return sc:IsXyzSummonable(g)
	elseif sc:IsType(TYPE_LINK) then
		return sc:IsLinkSummonable(g)
	end
	return false
end

function s.matfilter(g,sc)
	if not s.materialcheck(sc,g) then return false end

	return not g:IsExists(function(c,sg,sc)
		local g2=sg:Clone()
		g2:RemoveCard(c)
		return s.materialcheck(sc,g2)
	end,1,nil,g,sc)
end

function s.exfilter(c,mg_field,mg_fusion)

	if not c:IsSetCard(0xc50) then return false end

	if c:IsType(TYPE_FUSION) then
		return mg_fusion:CheckSubGroup(s.matfilter,1,#mg_fusion,c)
	else
		return mg_field:CheckSubGroup(s.matfilter,1,#mg_field,c)
	end
end

function s.selectmaterials(tp,mg,sc)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_MATERIAL)
	return mg:SelectSubGroup(tp,s.matfilter,false,1,#mg,sc)
end

function s.specialfromextra(tp,sc,mat)

	if Duel.GetLocationCountFromEx(tp,tp,mat,sc)<=0 then return end

	sc:SetMaterial(mat)

	local sumtype=SUMMON_TYPE_SPECIAL
	local reason=REASON_MATERIAL

	if sc:IsType(TYPE_FUSION) then
		sumtype=SUMMON_TYPE_FUSION
		reason=reason+REASON_FUSION
	elseif sc:IsType(TYPE_SYNCHRO) then
		sumtype=SUMMON_TYPE_SYNCHRO
		reason=reason+REASON_SYNCHRO
	elseif sc:IsType(TYPE_XYZ) then
		sumtype=SUMMON_TYPE_XYZ
	elseif sc:IsType(TYPE_LINK) then
		sumtype=SUMMON_TYPE_LINK
		reason=reason+REASON_LINK
	end

	if sc:IsType(TYPE_XYZ) then
		Duel.Overlay(sc,mat)
	elseif sc:IsType(TYPE_FUSION) then
		-- diferença principal: GY volta para o Deck
		local g1=mat:Filter(Card.IsLocation,nil,LOCATION_GRAVE)
		local g2=mat:Filter(Card.IsLocation,nil,LOCATION_HAND+LOCATION_MZONE)

		if #g1>0 then
			Duel.SendtoDeck(g1,nil,SEQ_DECKSHUFFLE,REASON_MATERIAL+REASON_FUSION)
		end
		if #g2>0 then
			Duel.SendtoGrave(g2,REASON_MATERIAL+REASON_FUSION)
		end
	else
		Duel.SendtoGrave(mat,reason)
	end

	Duel.SpecialSummon(sc,sumtype,tp,tp,false,false,POS_FACEUP)
	sc:CompleteProcedure()
end