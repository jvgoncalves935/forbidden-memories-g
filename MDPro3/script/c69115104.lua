--Pegasus do PAU BRILHANTE
--c69115104
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	c:SetUniqueOnField(1,0,id)

	--Xyz Summon procedure: 2 "Universo G" com diferença de nível exatamente 1
	aux.AddXyzProcedureLevelFree(c,s.mfilter,s.xyzcheck,2,2)
	
	--Alternate Xyz Summon: 2 Toon monsters (qualquer nível)
	local e0=Effect.CreateEffect(c)
	e0:SetDescription(aux.Stringid(id,3))
	e0:SetType(EFFECT_TYPE_FIELD)
	e0:SetCode(EFFECT_SPSUMMON_PROC)
	e0:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e0:SetRange(LOCATION_EXTRA)
	e0:SetCondition(s.toonxyzcon)
	e0:SetOperation(s.toonxyzop)
	c:RegisterEffect(e0)

	--Treat as "Mundo da PUTARIA" on the field
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_ADD_CODE)
	e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e1:SetRange(LOCATION_MZONE)
	e1:SetValue(69069069) -- Mundo da PUTARIA
	c:RegisterEffect(e1)

	--Rank is treated as highest Level of materials (visual effect)
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_XYZ_LEVEL)
	e2:SetValue(s.xyzlv)
	c:RegisterEffect(e2)

	--Quick Effect: detach 1 material, choose 1 effect
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetCategory(CATEGORY_TOHAND+CATEGORY_SPECIAL_SUMMON)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id)
	e3:SetCost(s.xyzcost)
	e3:SetTarget(s.xyztg)
	e3:SetOperation(s.xyzop)
	c:RegisterEffect(e3)

	--Quick Effect: equip 1 card from opponent field or grave
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,2))
	e4:SetCategory(CATEGORY_EQUIP)
	e4:SetType(EFFECT_TYPE_QUICK_O)
	e4:SetCode(EVENT_FREE_CHAIN)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCountLimit(1,id+100)
	e4:SetTarget(s.eqtg)
	e4:SetOperation(s.eqop)
	c:RegisterEffect(e4)
end

-- Xyz material filter: each required material must be "Universo G" monster
function s.mfilter(c,xyzc)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_MONSTER)
end

-- Xyz check: exactly 2 monsters and their level difference must be exactly 1
function s.xyzcheck(g,lc,tp)
	if g:GetCount()~=2 then return false end
	local tc1=g:GetFirst()
	local tc2=g:GetNext(tc1)
	if not tc1 or not tc2 then return false end
	-- both must have levels (not for Xyz materials like Tokens without level)
	if tc1:GetLevel()<=0 or tc2:GetLevel()<=0 then return false end
	-- difference exactly 1
	return math.abs(tc1:GetLevel() - tc2:GetLevel())==1
end

-- Toon Xyz Summon condition (2 Toon monsters on your field)
function s.toonxyzcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	return Duel.IsExistingMatchingCard(Card.IsType,tp,LOCATION_MZONE,0,2,nil,TYPE_TOON)
end

-- Toon Xyz Summon operation
function s.toonxyzop(e,tp,eg,ep,ev,re,r,rp,c)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local g=Duel.SelectMatchingCard(tp,Card.IsType,tp,LOCATION_MZONE,0,2,2,nil,TYPE_TOON)
	c:SetMaterial(g)
	Duel.Overlay(c,g)
end

-- Rank treated as highest Level among materials (visual)
function s.xyzlv(e,c,rc)
	local g=c:GetMaterial()
	local lv=0
	if not g then return 0 end
	for tc in aux.Next(g) do
		local l=tc:GetLevel() or 0
		if l>lv then lv=l end
	end
	return lv
end

-- Detach cost
function s.xyzcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():CheckRemoveOverlayCard(tp,1,REASON_COST) end
	e:GetHandler():RemoveOverlayCard(tp,1,1,REASON_COST)
end

-- Quick Effect target: choose effect 1 or 2
function s.xyztg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(id,3))
	e:SetLabel(Duel.SelectOption(tp,aux.Stringid(id,3),aux.Stringid(id,4)))
end

-- Quick Effect operation: resolve selected effect
function s.xyzop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	local sel=e:GetLabel()
	if sel==0 then
		-- Effect 1: add 1 Universo G (ou Toon? você pode alterar a condição) from Deck or Grave to hand
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
		local g=Duel.SelectMatchingCard(tp,aux.NecroValleyFilter(function(tc) return tc:IsSetCard(0xc50) and tc:IsType(TYPE_MONSTER) and tc:IsAbleToHand() end),tp,LOCATION_DECK+LOCATION_GRAVE,0,1,1,nil)
		if #g>0 then
			Duel.SendtoHand(g,nil,REASON_EFFECT)
			Duel.ConfirmCards(1-tp,g)
		end
	else
		-- Effect 2: Special Summon a material from its previous overlay (if any left)
		local og=e:GetHandler():GetOverlayGroup()
		if #og>0 then
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
			local sg=og:Select(tp,1,1,nil)
			if #sg>0 then
				Duel.SpecialSummon(sg,0,tp,tp,false,false,POS_FACEUP)
			end
		end
	end
end

-- Equip effect target
function s.eqtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsAbleToChangeControler,tp,0,LOCATION_ONFIELD+LOCATION_GRAVE,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_EQUIP,nil,1,tp,LOCATION_ONFIELD+LOCATION_GRAVE)
end

-- Equip operation
function s.eqop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EQUIP)
	local g=Duel.SelectMatchingCard(tp,Card.IsAbleToChangeControler,tp,0,LOCATION_ONFIELD+LOCATION_GRAVE,1,1,nil)
	local tc=g:GetFirst()
	if tc then
		if Duel.Equip(tp,tc,c,true) then
			-- Equip limit
			local e1=Effect.CreateEffect(c)
			e1:SetType(EFFECT_TYPE_SINGLE)
			e1:SetCode(EFFECT_EQUIP_LIMIT)
			e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
			e1:SetReset(RESET_EVENT+RESETS_STANDARD)
			e1:SetValue(function(ef,cc) return cc==c end)
			tc:RegisterEffect(e1)
			-- If equipped card is a monster, gain its ATK/DEF (text values)
			if tc:IsType(TYPE_MONSTER) then
				local atk=tc:GetTextAttack()
				local def=tc:GetTextDefense()
				if atk<0 then atk=0 end
				if def<0 then def=0 end
				local e2=Effect.CreateEffect(c)
				e2:SetType(EFFECT_TYPE_SINGLE)
				e2:SetCode(EFFECT_UPDATE_ATTACK)
				e2:SetValue(atk)
				e2:SetReset(RESET_EVENT+RESETS_STANDARD)
				c:RegisterEffect(e2)
				local e3=e2:Clone()
				e3:SetCode(EFFECT_UPDATE_DEFENSE)
				e3:SetValue(def)
				c:RegisterEffect(e3)
			end
		end
	end
end
