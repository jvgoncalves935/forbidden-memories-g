-- Jailson Mendes, O Primeiro Machinho
local s,id=GetID()

function s.initial_effect(c)
	c:EnableReviveLimit()

	-- Link Summon
	aux.AddLinkProcedure(
		c,
		s.matfilter, -- filtro de material
		4,4,nil		  -- exatamente 4 materiais
	)
end

function s.matfilter(c,lc,sumtype,tp)
	return c:IsSetCard(0xc50)
end

