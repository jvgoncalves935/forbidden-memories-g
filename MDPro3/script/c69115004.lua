--Índio (Indígena)
local s,id=GetID()
function s.initial_effect(c)
	-- Quick Synchro from hand
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE)
	e1:SetCountLimit(1,id) -- hard once per turn
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)
end

-- Deck material filter (Universo G monster)
function s.matfilter(c,needlv)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_MONSTER)
		and c:GetLevel()==needlv
end

function s.validscfilter(c,e,tp,handc)
	if not (c:IsSetCard(0xc50)
		and c:IsType(TYPE_SYNCHRO)
		and c:IsLevelBelow(6)
		and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_SYNCHRO,tp,false,false)) then
		return false
	end

	local needlv=c:GetLevel()-handc:GetLevel()
	if needlv<=0 then return false end

	return Duel.IsExistingMatchingCard(
		s.matfilter,tp,LOCATION_DECK,0,1,nil,needlv
	)
end


function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
		local sg=Duel.GetMatchingGroup(s.validscfilter,tp,LOCATION_EXTRA,0,nil,e,tp,c)
		return sg:IsExists(function(sc)
			local needlv=sc:GetLevel()-c:GetLevel()
			return needlv>0 and Duel.IsExistingMatchingCard(
				s.matfilter,tp,LOCATION_DECK,0,1,nil,needlv)
		end,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
end


function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	if not c:IsRelateToEffect(e) then return end

	-- escolhe o Sincro primeiro
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=Duel.SelectMatchingCard(tp,s.validscfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp,c):GetFirst()
	if not sc then return end

	local needlv=sc:GetLevel()-c:GetLevel()
	if needlv<=0 then return end

	-- escolhe o material correto do Deck
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SMATERIAL)
	local mg=Duel.SelectMatchingCard(tp,s.matfilter,tp,LOCATION_DECK,0,1,1,nil,needlv)
	local mc=mg:GetFirst()
	if not mc then return end

	-- envia materiais
	local mat=Group.FromCards(c,mc)
	Duel.SendtoGrave(mat,REASON_EFFECT+REASON_MATERIAL+REASON_SYNCHRO)

	-- invocação sincro manual
	sc:SetMaterial(mat)
	if Duel.SpecialSummon(sc,SUMMON_TYPE_SYNCHRO,tp,tp,false,false,POS_FACEUP)>0 then
		sc:CompleteProcedure()
	end

	-- Synchro Summon lock for the rest of the turn (engine-safe)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e1:SetTargetRange(1,0)
	e1:SetTarget(s.synclimit)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)

end

function s.synclimit(e,c,tp,sumtp,sumpos)
	return bit.band(sumtp,SUMMON_TYPE_SYNCHRO)==SUMMON_TYPE_SYNCHRO
end



